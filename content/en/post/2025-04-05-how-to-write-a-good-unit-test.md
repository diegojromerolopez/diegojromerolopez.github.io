---
title: How to write a good unit test
date: "2025-04-05T00:00:00+02:00"
draft: false
tags: ["software", "testing"]
---

# How to write a good unit test
This post provides some guidelines about how to write a good unit test.
There are some examples in Python with unittest.

## Introduction
In my last post I wrote about
[software quality](/blog/2025/03/software-quality-is-not-negotiable/)
not being taken seriously sometimes.

Tests are a good part of the *software quality* so I wanted to write a bit
about the testing effort we should be doing in our code.

Having said that, let us delve in the unit testing world with some examples in Python!

## What is a unit test?
A unit test is a test that checks the immediate dependencies of a module.

For example, given this simple function that makes a HTTP request to an URL:

```python
# api/health.py
import requests
from logging import Logger

def service_is_healthy(service_name: str, logger: Logger) -> bool:
    response = requests.get('https://{service_name}.example.com/health')
    ok = response.status_code == 200
    if ok:
        logger.info(f'Service {service_name} is healthy')
    else:
        logger.error(f'Service {service_name} is not healthy')
    return ok

```

A unit test would be something like the following one:

```python
from unittest import TestCase
from unittest.mock import MagicMock, patch


class TestApiHealth(TestCase):
    @patch('api.health.requests.get')
    def test(self, mock_requests_get: MagicMock):
        service_name = 'my-service'
        logger = logging.getLogger(__name__)
        
        mock_requests_get.return_value = MagicMock(status_code=200)
        
        healthy = service_is_healthy(service_name=service_name, logger=logger)

        self.assertTrue(healthy)
```

The immediate dependency (requests) is replaced by a mock dependency that we can modify
to change the behavior of our tested function.

## What is a good unit test?
It seems simple, we just check:

- What are we calling.
- How are we calling it.

It as simple as checking the immediate lower layer from the piece of code we want to test.

### Test name
*Naming is the hardest problem in ~~Computer Science~~ Software Engineering*, so we need
to provide a name that is meaningful and it actually helps the engineers to identify what
it checks.

A good candidate for our example is `test_service_is_healthy_status_ok`.

### Mock the dependencies
Unless we are talking about a Singleton that is extremely hard to mock,
**all dependencies must be mocked**.

Thus, it is easy to know the dependencies just by looking at the patch decorators:

```python
    @patch('api.health.requests.get')
    def test_service_is_healthy_status_ok(self, mock_requests_get: MagicMock, mock_logger: MagicMock):
        ...
```

### Exhaustive
In this context what I mean by exhaustive is that all the dependencies must have their
contracts checked. By contracts I mean the API calls.

So, if you have two mocks in your test, you would need to add assertions for each mock that check
not only the number of calls but the arguments of each call. If you do this that way you are ensuring
the contract between your module and the lower-level layer.

```python
    @patch('api.health.requests.get')
    @patch('api.health.Logger')
    def test_service_is_healthy_status_ok(self, mock_requests_get: MagicMock, mock_logger: MagicMock):
        service_name = 'my-service'

        mock_requests_get.return_value = MagicMock(status_code=200)

        healthy = service_is_healthy(service_name=service_name)
        
        self.assertTrue(healthy)
        self.assertEqual([call(f'https://{service_name}.example.com/health')], mock_requests_get.call_args_list)
        self.assertEqual([call(f'Service {service_name} is healthy'), mock_logger.info.call_args_list]) 
```

### Minimal
A test must check the least assertions as possible. I am not talking about having tests
for each of the assertions, but for the *group of assertions*.

For example, if we intend to test if logging messages are written, do not create
a test for each span expectation, but one test for all of them.

```python
    @patch('api.health.requests.get')
    @patch('api.health.Logger')
    def test_logging_when_service_is_healthy_status_ok(self, mock_requests_get: MagicMock, mock_logger: MagicMock):
        service_name = 'my-service'

        mock_requests_get.return_value = MagicMock(status_code=200)

        healthy = service_is_healthy(service_name=service_name)
        
        self.assertTrue(healthy)
        self.assertEqual([call(f'Service {service_name} is healthy')], mock_logger.info.call_args_list]) 
```

```python
    @patch('api.health.requests.get')
    @patch('api.health.Logger')
    def test_logging_when_service_is_healthy_status_internal_server_error(self, mock_requests_get: MagicMock, mock_logger: MagicMock):
        service_name = 'my-service'

        mock_requests_get.return_value = MagicMock(status_code=500)
        
        healthy = service_is_healthy(service_name=service_name)
        
        self.assertFalse(healthy)
        self.assertEqual([call(f'Service {service_name} is not healthy')], mock_logger.error.call_args_list]) 
```

Why do we need to leave the `assertTrue` or `assertFalse`? We need a *hook* to ensure the function is running as expected, and as leaving
that check is not much work, I always recommend ensuring that the behavior is the expected one in all tests.

### Check what not happens
It is important to check what happens but also **what does not happen**.

Coming back to our example, ensuring that the error log is not written at all when everything works perfectly is paramount:

```python
    @patch('api.health.requests.get')
    @patch('api.health.Logger')
    def test_logging_when_service_is_healthy_status_ok(self, mock_requests_get: MagicMock, mock_logger: MagicMock):
        service_name = 'my-service'

        healthy = service_is_healthy(service_name=service_name)
        
        self.assertTrue(healthy)
        self.assertEqual([call(f'Service {service_name} is healthy')], mock_logger.info.call_args_list]) 
        self.assertEqual([], mock_logger.error.call_args_list]) 
```

### External dependencies
This is a personal preference but **I do not like having to install packages for testing my projects**.

This is why I would rather use [unittest](https://docs.python.org/3/library/unittest.html) than
[pytest](https://docs.pytest.org/en/stable/) in Python. I know there are others that do not think
like me, but having another package whose upgrades, deprecations and removals need to be taking
care of is not worth it for me.

Other languages like Ruby where there is *some consensus*
in the community to use another one ([rspec](https://rspec.info/)). I think I have never used
[Test::Unit](https://ruby-doc.org/stdlib-3.1.0/libdoc/test-unit/rdoc/Test/Unit.html) in all
the years I have worked with Ruby.

I recommend using the most popular and (if possible built-in) testing package of your
programming language or framework you are basing your project on.

## Conclusion
Hope this short article has given you some pointers about how to create a good and useful unit test.
