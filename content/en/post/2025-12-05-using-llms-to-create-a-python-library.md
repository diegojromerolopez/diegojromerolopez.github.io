---
title: Using LLMs to create a python library
date: "2025-12-05T00:00:00+02:00"
draft: false
tags: ["llm", "ai", "war-story"]
---

# Using LLMs to create a python library
I have used Gemini and Claude [LLM](https://en.wikipedia.org/wiki/Large_language_model)
models to create a [mypy](https://mypy-lang.org/) plugin to mark a function as pure:
[mypy-pure](https://github.com/diegojromerolopez/mypy-pure).

## Introduction
I think that static analysis in Python is a great opportunity to catch a lot of issues
before running the program.

I do not even remember when, but I saw
[a thread in the Python official forum](https://discuss.python.org/t/static-typing-specify-if-function-is-pure/98392)
where a user was suggesting this `@pure` decorator idea to the Steering Council of Python.

The idea got lost in the conversation, the *pros*, the *cons*, etc. But I liked the idea and got me thinking.

## The idea
Some weeks ago I asked ChatGPT about creating an empty decorator in Python (`@pure`), and using it
to mark the functions in a special way. It showed me some code that I copied, studied and
understood (The AST visitors are not the easiest part of the standard Python library).

My idea was to leverage [mypy](https://mypy-lang.org/), and check that if the
function had the `@pure` decorator, it could not call to functions that were not pure.

I know that pure functions apart from not having side-effects, must return the same value
for the same inputs, but I decided to ignore that part because it was going to be difficult
to check that statically. On the other hand, checking if a function had side-effects was relatively
easy, as we only need to check if a function calls a subset of *impure* functions
of the Python standard library.

Anyhow, I abandoned the idea because I did not have time, and was not even sure about
the usefulness of this functionality.

## The final push
Google had released [Antigravity](https://antigravity.google/),
a new and shiny editor with AI agent integration, and a generous free tier.
I thought to myself, could I implement this library by
leveraging LLMs capabilities?

## The development
I decided to spend two hours each day having a conversation with a LLM I started seeing results.

The first day I had a decorator that was able to detect if a function was calling
an impure function directly.

The next day I was able to check if any of the ancestor called functions by a function was *impure*.

In 4 days I had the 0.2.1 with support for:

Support for marking as `@pure` functions:
  - Properties (`@property`)
  - Instance methods
  - Class methods (`@classmethod`)
  - Static methods (`@staticmethod`)
  - Async functions (`async def`)
  - Async methods
  - Nested/inner functions

Blacklisted standard functions (impure): 230+ impure functions including:
  - All major stdlib modules (logging, threading, multiprocessing, signal, etc.)
  - Network operations (http.client, urllib, ftplib, smtplib, etc.)
  - Database operations (sqlite3, dbm, shelve)
  - File operations (tempfile, pickle, pathlib)
  - System operations (gc, warnings, atexit)

## The released product
At the end of the day, I have an useful library that can detect use of functions with
side-effects when running mypy on your code.

### Install the library from [pypi](https://pypi.org/project/mypy-pure/).

```bash
pip install mypy-pure
```

### Enable the plugin in your mypy configuration

In your `mypy.ini` or `pyproject.toml` add mypy_pure to your list of plugins:

```ini
[mypy]
plugins = mypy_pure.plugin
```

### Add a list of your known pure impure functions to your `mypy.ini` or `pyproject.toml`

In your `mypy.ini` or `pyproject.toml` you can optionally define a list of impure or pure functions.

```ini
[mypy-pure]
# Blacklist your impure functions
impure_functions = my_module.send_email, my_module.log_event

# Whitelist pure third-party functions
pure_functions = requests.utils.quote, requests.utils.unquote
```

### Use the `@pure` decorator on your functions

```python
from mypy_pure import pure

@pure
def calculate_total(prices: list[float], tax_rate: float) -> float:
    subtotal = sum(prices)
    return subtotal * (1 + tax_rate)
```

## Caveats
### The LLM will always try to take the easiest step
Yes, the LLMs are lazy and tend to remove, and ignore complete pieces of code.

### You need to navigate the conversation
Sometimes, the LLMs hallucinate or worse, they propose removing features that clash with their view.
*You need to be at the helm* of the process, so in every change they propose, you can
steer their actions to what you actually want.

And everything of that without taking in account proposals that, while being 

### There is no agreement on what the license could be for that code
I even [asked Reddit](https://www.reddit.com/r/Python/comments/1pac4x0/what_should_be_the_license_of_a_library_created/) about this!

Some people say that the LLMs memorize code with different license, hence
producing some pieces of code that came from projects with incompatible licenses. 

To be fair, I think that we have reached the point of *practicality*, and assumed
that the LLMs just read everything and just adjust their weights from all they
get their hands on.

I have not seen any *regurgitated* piece of code, but that is what they say.

My project has the MIT license and I will defend it arguing:

- No financial gain.
- [Fair use](https://en.wikipedia.org/wiki/Fair_use).

## Conclusion
The development velocity with LLMs is surprising: what could have been 1 month of development
was done by the LLM and checked by me, in hours.

The legality of the code still seems to be an issue.