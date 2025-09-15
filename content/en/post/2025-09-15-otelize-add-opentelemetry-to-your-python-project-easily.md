---
title: Otelize, add OpenTelemetry to your Python project easily
date: "2025-09-15T00:00:00+02:00"
draft: false
tags: ["python", "package", "software", "monitorization", "telemetry"]
---

# Otelize, add OpenTelemetry to your Python project easily
OpenTelemetry (sometimes abbreviated as OTEL) is a standard for telemetry
and monitorization of software applications that has gain a lot of traction in these last years.
We will learn here how to use the Python package [otelize](https://github.com/diegojromerolopez/otelize)
to add this telemetry to our Python applications without having to rely on much boilerplate.

## How did I use to add OTEL telemetry to my Python code?
Just by adding a lot of spans (at least one per function). This is done by relying on the context manager
that is provided by the [opentelemetry-api](https://pypi.org/project/opentelemetry-api/) package.

```python
def your_function():
    with tracer.start_as_current_span('your_function') as span:
        # your code sentences
        span.set_attributes({'an': 'attribute'})
        # your code sentences
        span.set_attributes({'another': 'attribute'})

        for _ in your_iterable:
            with tracer.start_as_current_span('your_function') as span:
                # your code sentences
                span.set_attributes({'an': 'attribute', 'in_the': 'loop'})
                # your code sentences
```

As you can guess, this continuos use of context managers worsens the readability of the code
and *pollutes* the code with this *explicit monitorization*.

## Otelize

## Rationale
I am very eager to add a span per function to ease the debugging process of systems in production.
Just seeing the cascade of function calls reduces my anxiety when dealing with a bug.

For each function span, I usually add the input arguments and any other context information that could be
useful for the future developer that is fixing the issue in production.

I also add a span in each loop and conditional (mostly when they end up returning a value and hence,
exiting the function scope).

## What is Otelize?
A [Python package](https://pypi.org/project/otelize/) with a collection of utilities with the intent of provide
some helper tools to ease the pain of adding opentelemetry instrumentation to your custom code.

As there is already [zero-code auto-instrumentation exists for the most popular Python libraries](https://opentelemetry.io/docs/zero-code/python/), I wanted to provide a way to add a basic instrumentation for Python code that needs to have a custom
instrumentation.

So I decided to create a decorator, and some functions that could *extend* the current code by adding a basic OTEL layer.

### Features

#### Function/Class decorator

Usually when you want to add a span with some attributes to a function, in Python
you use a context manager and add the span attributes or events that you desire.
Something like this:

```python
import json

from opentelemetry import trace

tracer = trace.get_tracer(__name__)

def your_function(a_param: str, another_param: int, a_list: list[float], a_dict: dict[str, str]):
    with tracer.start_as_current_span('your_function') as span:
        span.set_attributes(...)
        span.add_event(...)
        # Your code
```

The problem with this approach is that it requires a lot of boiler plate and it becomes
cumbersome after adding theses OpenTelemetry code to every function again and again.

That is why the `@otelize` decorator does this for you. Just by adding the otelize
decorator to your function will create an automatic span and will set the function arguments
as attributes of the span.

So by adding the decorator:

```python
@otelize
def your_function(a_param: str, another_param: int, a_list: list[float], a_dict: dict[str, str]):
```

We are actually wrapping all its contents with a span that passes all his positional and keyword arguments
as span attributes:


```python
@otelize
def your_function(a_param: str, another_param: int, a_list: list[float], a_dict: dict[str, str]):
```

So a positional-only argument call of this function

```python
your_function('a_param', 2, [1., -2.5, 3.0], {'debug': True})
```

will cause the code to be like this:

```python
import json

from opentelemetry import trace

tracer = trace.get_tracer(__name__)

def your_function(a_param: str, another_param: int, a_list: list[float], a_dict: dict[str, str]):
    with tracer.start_as_current_span('your_function') as span:
        span.set_attributes({
            'function.call.arg.a_param.value': a_param,
            'function.call.arg.another_param.value': another_param,
            'function.call.arg.a_list.value': json.dumps(a_list),
            'function.call.arg.a_dict.value': json.dumps(a_dict),
            'function.call.return.value': return_value,
        })
```

And a keyword-only argument call of this function

```python
your_function(a_param='param', another_param=2, a_list-[1., -2.5, 3.0], a_dict={'debug': True})
```

will cause the code to be like this:

```python
import json

from opentelemetry import trace

tracer = trace.get_tracer(__name__)

def your_function(a_param: str, another_param: int, a_list: list[float], a_dict: dict[str, str]):
    with tracer.start_as_current_span('your_function') as span:
        span.set_attributes({
            'function.call.arg.a_param.value': a_param,
            'function.call.arg.another_param.value': another_param,
            'function.call.arg.a_list.value': json.dumps(a_list),
            'function.call.arg.a_dict.value': json.dumps(a_dict),
            'return.value': return_value,
        })
```

**The decorator works for classes too**, it is dynamically applied to all methods of the class.
There is several things to take in consideration:

1. The dunder methods are ignored.
2. The implicit parameter (`self` or `cls` are ignored for instance or class methods respectively).

So, for example for this HttpClient class:

```python
import requests
from otelize import otelize


class HttpClient:
    def __init__(self, base_url: str, headers: dict[str, str] | None = None):
        self.__base_url = base_url.rstrip("/")
        self.__session = requests.Session()
        self.__headers = headers or {}
        self.__session.headers.update(self.__headers)

    @otelize
    def get(self, path: str, params: dict[str, str] | None = None) -> requests.Response:
        url = f"{self.base_url}/{path.lstrip('/')}"
        response = self.__session.get(url, params=params)
        response.raise_for_status()
        return response
    
    # ...
```

The method get would have its code instrumentalized as if it was a decorated function.

#### Iterator instrumentation
Apart from functions, another use that is common is to wrap the contents of a loop in an
OpenTelemetry span, e.g.

```python
items = ['first', 'second', 'third']
for item in items:
    with tracer.start_as_current_span('your_function') as item_loop_span:
        item_loop_span.set_attributes({'item.value': item})
        
        result = do_something(item)
        item_loop_span.set_attributes({'result.value': result})

        # ...
```

The `start_as_current_span` context manager makes the loop code difficult to understand.
Yes, in this example the intent is clear and the OTEL code is not too much.

I wanted to have a tool to wrap the loop à la enumerate, to free the developer
of having to define the span by hand.

```python
from otelize import otelize_iterable

a_list = ['first', 'second', 'third']
for item_span, item in otelize_iterable(a_list):
    item_span.set_attributes({'item_again': item})
```

Of course, the custom attributes still
need to be added manually, but it is an improvement over having to write
the context manager and indent the code.

#### Context manager instrumentation
Python provides the developer with context managers to encapsulate common
behaviors before and after a block of code.

So we provide a `otelize_context_manager` function that adds a span to the
variables returned by a context manager.

For example, the following creation of temporal file is done via the tempfile module
utilities, and we have decided to wrap the context manager in the `otelize_context_manager`
function to have a span available for adding some span custom attributes:

```python
import os
import tempfile

with otelize_context_manager(tempfile.NamedTemporaryFile()) as (temp_file_span, temp_file):
    temp_file.write(b'hello')
    # more writing ...
    temp_file.flush()

    temp_file_span.set_attributes({
        'temp_file.size': os.path.getsize(temp_file.name)
    })
```

#### OTEL values
Not all the values should be added to our monitorization efforts.
It does not matter if they are in span attributes or events, they should not be
sent without any conversion to our monitorization provider.

##### Sequences, dictionaries, sets and other data structures
First, there are values that are complex data structures and would not be understood
by our monitorization providers. That is why otelize serializes dictionaries, lists,
and sets with **JSON serialization**.

The [OtelValueConverter](https://github.com/diegojromerolopez/otelize/blob/main/otelize/adapters/otel_value_converter.py)
adapter deals with converting any kind of value to a proper (and useful) value for our OTEL provider

##### Secret information
Second, there are some secrets, tokens or information that should not be divulged to an external entity.
It can be an authentication token, a password, or any kind of information that we want to redact.

To do it, otelize provides the possibility of telling the package what are the attribute names that should be
redacted. otelize will read from these two environment variables:

- `OTELIZE_SPAN_REDACTABLE_ATTRIBUTES`: a JSON-serialized array of strings with the attributes that need to be redacted.
- `OTELIZE_SPAN_REDACTABLE_ATTRIBUTES_REGEX`: a string with a Python regex that will be used to match sensible attributes.

and will use these two environment variables to check if an attribute needs to be redacted.

The redacted values will take the value `[REDACTED]` in our provider. That way we show that the attribute was there,
but we do not leak the value.

## What is missing?
There are some ideas that I would like to implement in the next releases:

### Positional and keyword arguments
Do we really need to make a distinction among them?

### Async support
I could colorize my functions depending on if they are async or not.

### Secret value detection
If you pass a token with a positional argument it will be leaked to the monitoring provider.

### Exceptions
We are just doing nothing. We should allow catching a list of expected exceptions.

## Conclusion
[otelize](https://github.com/diegojromerolopez/otelize) is a simple,
easy and useful package to add to your project when you do
not know exactly what to monitorize or you want to monitorize all the function calls,
loops and context managers.
