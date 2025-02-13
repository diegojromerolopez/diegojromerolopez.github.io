---
title: Patching on setUp in Python's unittest
date: "2025-02-13T00:00:00+02:00"
draft: false
tags: ["python", "unittest"]
---

# Patching on setUp in Python's unittest
One of my favorite programming languages is Python,
and I think that tests should be a foundational part
of software development, so it is not strange that I
delve a lot in Python's unittest.

In this post we are going to show how to use `unittest.mock.patch`
not in a decorator (the usual case) but in the `setUp` method.

## Why should you care about this?
Well, I have not cared about this after more than a decade of
working with python (intermittently), because I was just used
to the patch decorator. However, we can stop repeating the code
and save some precious space (and possible bugs) if we just
re-use the code by injecting some code in the `setUp` method.

## But I use pytest so I am not interested in this
I would rather have the minimal dependencies
in my projects and not depend on any package that is not needed 100%.

[unittest](https://docs.python.org/3/library/unittest.html) comes from
the standard library of Python so I prefer to use it
unless there is a hard requirement to use pytest.

However, *to each its own*, if you are happy with pytest that is perfect
and I am glad you feel that way.

## What is this setUp method?
There are two methods for preparing the environment for the test in unittest:

- `setUp` runs before each test.
- `setUpClass` runs once before all tests.

In our case we are going to assign to the implicit object (`self`) some mocks
to have it ready for each test method.

Analogously there are two methods for cleaning up the resources we have initialized:

- `tearDown` runs after each test.
- `tearDownClass` runs once after all tests.

By the way, notice that the methods are camelCase, hence not following the
snake_case convention.

## How can I patch methods/classes in setup?

```python
import unittest


class TestCase(unittest.TestCase):
    def setUp(self):
        my_patcher = patch('module.path.object')
        self.mock_func = my_patcher.start()
        self.addCleanup(my_patcher.stop)

    def test(self):
        self.mock_func.return_value = 2

        function_that_calls_to_module_path_object()

        self.assertEqual([call()], self.mock_func.call_args_list)

```

### An example: patching GET requests

Let suppose we are building a dictionary wrapper and we are going to query the `dictionaryapi.dev` API.

We first create a function to get word definitions:

```python
# dictionary/definition.py
from typing import Any

import requests


def get_word_definition(word: str) -> list[dict[str, Any]]:
    try:
        response = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}')
        return response.json()
    except RequestException as exception:
        raise DictionaryException(
            f'Word meaning for {word} could not be obtained. Exception: {exception.__class__.__name__}'
        ) from exception
```

But we want to test that we call to the get method of requests and that, in case of an exception,
we are prepared:

```python
# dictionary/tests/test_definition.py
import unittest
from unittest.mock import MagicMock, patch

from requests.exceptions import Timeout

from dictionary.definition import get_word_definition, DictionaryException


class TestDefinition(unittest.TestCase):
    def setUp(self):
        requests_patcher = patch('dictionary.definition.requests')
        self.mock_requests = requests_patcher.start()
        self.addCleanup(mock_requests.stop)

    def test_get_word_definition_success(self):
        expected_response = [
            {
                'word': 'house'
            }
        ]

        word = 'house'

        mock_response = MagicMock()
        mock_response.json.return_value = expected_response
        self.mock_requests.get.return_value = mock_response

        response = get_word_definition(word)

        self.assertEqual(expected_response, response)
        self.assertEqual([call(word)], self.mock_requests.get.call_args_list)
        self.assertEqual([call()], mock_response.json.call_args_list)

    def test_get_word_definition_timeout(self):
        word = 'house'

        self.mock_requests.get.side_effect = Timeout()

        with self.assertRaises(DictionaryException) as context:
            get_word_definition(word)

        self.assertEqual(
            f'Word meaning for {word} could not be obtained. Exception: Timeout',
            str(context.exception)
        )
        self.assertEqual([call(word)], self.mock_requests.get.call_args_list)
```

As you see above, we have a `self.mock_requests` instance attribute that contains
a mock to the requests library. In this case you could argue that the gains are not
much, but imagine if the `get_word_definition` would have 3 dependencies that need
to be tested, so you could save a lot of repeated code by using this technique.

## Conclusion
We have shown how to patch in the setUp method, this is useful for sharing
mocks between several tests, hence keeping the minimal code in each one
of the test methods.
