---
title: Don't use singletons
date: "2024-11-10T00:00:00+02:00"
draft: false
tags: ["software", "architecture", "anti-pattern"]
---

# Don't use singletons
The Singleton pattern is one of the patterns that appeared
in the [Design Patterns book by Erich Gamma et al.](https://en.wikipedia.org/wiki/Design_Patterns).

## What is a singleton?
The singleton is one design patter to share a resource in a controlled manner
in a code base. That resource could be a configuration, a connection or any other
global state that should be unique.

## How to implement it?

There are several ways to implement this, but in Python (for example)
you can implement it by making use of the [Python metaclasses](https://realpython.com/python-metaclasses/).

For example (see the source and other possible alternative implementations [in this StackOverflow question](https://stackoverflow.com/questions/6760685/what-is-the-best-way-of-implementing-singleton-in-python)):

```python
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
```

## How to use it?

For example we could define a singleton over the Logger object in Python:

```python
from logging import Formatter, Logger, StreamHandler
from singleton import Singleton

class BasicLogger(Logger, metaclass=Singleton):
    def __init__(self, level=NOTSET):
        super().__init__('BasicLogger', level=level)

        formatter = Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler = StreamHandler(sys.stdout)
        handler.setFormatter(formatter)

        self.addHandler(handler)
```

So anytime we instantiate the logger, the object is the same:

```python
logger1 = BasicLogger()
logger2 = BasicLogger()
assert(id(logger1) == id(logger2))
```

## Why you shouldn't use it?

There are a lot of reasons why you should not use Singletons.
There are several posts and pages that have arged in that direction:

- [The Singleton; a Dangerously Overused Pattern
](https://timjwilliams.medium.com/the-singleton-a-dangerously-overused-pattern-d4007758bca2)
- [Singletons Considered Harmful](https://kentonshouse.com/singletons)

There are a lot of reasons that could be enumerated here:
- They are just global state.
- They do not follow the single responsibility principle.
- Most implementations do not take in account the [open/closed principle](https://en.wikipedia.org/wiki/Open%E2%80%93closed_principle).
- They could harbour hidden dependencies.

Etc, etc. Let's suppose that we don't care about code quality
(we should). However, there is a practical reason to avoid singletons:
**they are difficult to deal with in the tests**.

## Testing singletons: a nightmare

### A singleton test

How can you test a component that relies on a global object, that is
hidden from plain sight?
- Should you just mock the object for all tests? Not easy in Python (unittest).
- Should you initialize it before each test? That would be similar to
implementing an integration tests, right?

Let's see an example of a class that uses a singleton:

```python
from logger import BasicLogger
from logging import DEBUG


class User:
    def __init__(self, debug: bool = None):
        self.__logger = BasicLogger()
        if debug:
            self.__logger.setLevel(DEBUG)
        # ...
```

A very simplet test could be:

```python
from unittest import MagicMock, TestCase, call
from logging import Logger


class TestUser(TestCase):
    def setUp(self):
        BasicLogger().setLevel(INFO)

    def test_debug_true(self):
        user = User(logger=BasicLogger(), debug=True)

        self.assertEquals(BasicLogger().level, DEBUG)

    def test_debug_none(self, mock_logger):
        user = User(logger=BasicLogger(), debug=None)

        self.assertEquals(BasicLogger().level, INFO)
```

However, in this case this works because the logger is pretty simple but if we modify
the level of the logger, it will affect all other tests, hence making them fail.

Before any of you readers tell it, there is the possibility of patching the import of the BaseLogger. However,
what about other uses of the logger in other components? **Any use of BaseLogger should be mocked independently**.

### A dependency injection test

Compare with just passing the dependencies in the constructor of the class, it is
trivial to mock the dependencies and just implement the unit test behaviour check:

```python
from logging import DEBUG

class User:
    def __init__(self, logger: Logger):
        self.__logger = logger
        if debug:
            self.__logger.setLevel(DEBUG)
        # ...

```

```python
from unittest import MagicMock, TestCase, call
from logging import Logger, DEBUG, INFO


class TestUser(TestCase):
    def test_debug_true(self):
        expected_serialized_user = json
        logger = BasicLogger()

        user = User(logger=logger, debug=True)

        self.assertEquals(logger.level, DEBUG)

    def test_debug_none(self):
        expected_serialized_user = json
        logger = BasicLogger()

        user = User(logger=logger, debug=None)

        self.assertEquals(logger.level, INFO)
```

## Conclusion
This post shows several reasons why singletons should be avoided. It also focus on
testing, because singletons make testing much harder. An example of using dependency
injection instead is also shown.
