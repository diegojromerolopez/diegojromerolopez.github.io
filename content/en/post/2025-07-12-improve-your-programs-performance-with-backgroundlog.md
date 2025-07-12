---
title: Improve your programs performance with backgroundlog
date: "2025-07-12T00:00:00+02:00"
draft: false
tags: ["software", "library"]
---

# Improve your programs performance with backgroundlog
[backgroundlog](https://github.com/diegojromerolopez/backgroundlog) is a library that
allows you to use a background thread to write log messages.
The idea for that is to be transparent to the developer, in the sense that they do not need
to worry about async functions, the event loop, or managing threads.

## Introduction
The other day I was having a conversation with another software engineer about how to read lines
from a file and write in another file in the most performant way possible. Take in account that
the file was supposed to have several GB of information and we could not block the flow.

When you face this kind of issues, the basic solution is to use some kind of thread that can be
unblock the main flow. In the case of the file, there was also the difficulty of having
to keep the order, but more or less, expensive I/O operations usually means threads.

This got me thinking that threading has the issues we all know: synchronization and sharing
information. But, what about the operations that did not have any of those? What about
I/O operations that we need to do but whose result we are not interested?
Could we *embarrassingly* implement something to provide tiny improvements to the main program flow?

## Logs
So that got me to the logs. The logs are usually written in disk, and is an operation that is repeated many times.
We also write logs in our programs and we do not consider the cost of that when we have loops or many log calls.

In the case of OTEL, the opentelemetry library groups several spans in a batch and delivers
it to the OTEL collector with background threads.

Could I just do the same with the logs but removing the batch writes?
Even easier than what the opentelemetry developers created.

## The design
My first thought is to make use of the async create_task, but the virality nature of async makes it one
of my not-favorite things.

### Wrapping a logging handler

I also wanted to pass a standard [logging handler](https://docs.python.org/3/library/logging.handlers.html)
to this new background thread-based handler to avoid having to worry about how the log records are
actually delivered (*emitted* in the jargon of Python logging). Why should the responsibility of the emission
of the log records be owned by a threaded managing system? Let's not mix things up.

So I decided to just pass a logging handler to the initializer:

```python
 def __init__(
        self,
        wrapped_handler: Handler,
        # ...
    ) -> None:
    ...
```

### Using a synchronized queue

So I decided to use a background thread with a queue, and process the logging records in an ordered fashion.
To enforce this order, I would just use a [Python queue](https://docs.python.org/3/library/queue.html).
It is thread-safe and provide a way of keeping the log record order.

```python
        # Inside the __init__ method
        self.__queue: Queue[LogRecord] = Queue(maxsize=queue_size)
```

### The main actor:  the background thread

The main idea is to put the log records in the queue and have a thread get the items from the queue and
*emit* (usually write to disk).

```python
    # This is the background thread loop
    def __feeder_loop(self) -> None:
        while not self.__stop_event.is_set() or not self.__queue.empty():
            try:
                record = self.__queue.get(
                    block=True,
                    timeout=self.__flush_interval,
                )
                self.__handle(record)
            except Empty:
                continue
```

Of course this could be improved by grouping the log records, but I do not care for this first version.

The __handle method is just calling to the wrapped handler emit method (writing to a disk, usually):

```python
    def __handle(self, record: LogRecord) -> None:
        try:
            self.__wrapped_handler.emit(record)
        except self.EMIT_ERRORS:
            self.__wrapped_handler.handleError(record)
```

## And what about the possible issues?
I decided to do a clear separation among the log entries that we can afford to lose, and the ones that not.
The critical and error messages cannot be lost, the others... Well, in the event of a catastrophe, they could be.

So I decided to allow some configurability about what should be done in the case of some log records of the desired
levels not be able to be delivered to the internal queue:

```python
    # Overwriting of the logging.Handler emit method
    def emit(self, record: LogRecord) -> None:
        if record.levelno in self.__blocking_levels:
            self.__blocking_queue_put(record=record)
        else:
            self.__non_blocking_queue_put(record=record)
```

We could define some critical levels that need to be writen to the queue, the others could be lost.

```python
    # The initializer of the ThreadHandler where you could define what levels need to have a blocking
    # delivery to the queue
    def __init__(
        self,
        wrapped_handler: Handler,
        queue_size: int = DEFAULT_QUEUE_SIZE,
        blocking_levels: set[int] | None = None,
        blocking_timeout: float | None = None,
    ) -> None:
    ...
```

## End of act
What I did not have very clear was the cleaning up of the used resources, luckily, we have a
way of defining functions to run at the termination of the program by using
[atexit](https://docs.python.org/es/3/library/atexit.html).

So by leveraging atexit, we could register a private method to be run at termination:

```python
    def __init__(
        self,
        wrapped_handler: Handler,
        queue_size: int = DEFAULT_QUEUE_SIZE,
        blocking_levels: set[int] | None = None,
        blocking_timeout: float | None = None,
        flush_interval: float = DEFAULT_FLUSH_INTERVAL,
        shutdown_timeout: float | None = DEFAULT_SHUTDOWN_TIMEOUT,
    ) -> None:
        super().__init__()
        # ...
        atexit.register(self.__close)

```

And the cleaning up function, that sends the stop event to the thread and
waits until it ends.

It also closes the logging handler.

```python
    def __close(self) -> None:
        self.__stop_event.set()
        self.__feeder.join(timeout=self.__shutdown_timeout)
        self.__wrapped_handler.close()
        super().close()

```

## Performance improvements

By running a 100K log messages in a loop, I have obtained the following performance gains:

### Python 3.15.3 (with GIL)
```
| Logging Handler               | Spent Time     |              | vs. Baseline |
|-------------------------------|----------------|--------------|--------------|
|                               | Mean Time (ms) | Std Dev (ms) |              |
| StreamHandler                 | 0.685          | 0.006        | baseline     |
| FileHandler                   | 0.685          | 0.018        | +0.03%       |
| ThreadHandler (StreamHandler) | 0.487          | 0.03         | -28.911%     |
| ThreadHandler (FileHandler)   | 0.475          | 0.002        | -30.66%      |
```

There is a ~30% of improvement when running the thread handler.

### Python 3.15.3t (without GIL)
```
| Logging Handler               | Spent Time     |              | vs. Baseline |
|-------------------------------|----------------|--------------|--------------|
|                               | Mean Time (ms) | Std Dev (ms) |              |
| StreamHandler                 | 0.539          | 0.004        | baseline     |
| FileHandler                   | 0.545          | 0.013        | +1.109%      |
| ThreadHandler (StreamHandler) | 0.344          | 0.002        | -36.301%     |
| ThreadHandler (FileHandler)   | 0.339          | 0.001        | -37.118%     |
```

There is a ~36% of improvement when running the thread handler. +6% with respect of the
Python version with GIL.

## Conclusion
I have created a simple library that allows you to send a the logging writes to a background thread.
The performance gains are of about 30%-36% of time.

I want to continue working on that, and I am open to feedback!