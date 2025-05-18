---
title: I do not like *args and **kwargs in Python
date: "2025-05-18T00:00:00+02:00"
draft: false
tags: ["software", "python", "conventions"]
---

# I do not like *args and **kwargs in Python
`*args` and `**kwargs` are the way to declare positional and keyword function arguments (resp.) in Python.

## Introduction
This post explains why I am a fan of naming the arguments and I do not like positional arguments nor
the `*args` and `**kwargs` way of passing arguments.

## Why I don't like *args and **kwargs?
Most of the time I only use `*args` and `**kwargs` when strictly necessary, like when inheriting from a class
that uses them, and I need to pass the parameters to the parent class. Most of the time,
**I would rater add 10 parameters with a default value than leaving an unknown interface in a function**.

That is what I try to do in my codebase: making everything as explicit as possible.
However, some people have a different idea, and implement things differently.

I have been working for a while with a Python library that provides an interface to an API of a
popular code repository service. All the methods use `*args` and `**kwargs` arguments as they are implemented
in common mixins. This has lead to issues, and having a difficult type when checking the types.

Below the main points that explain my posture:

### It looks like magic
If I approach a function and see some `*args` and `**kwargs` parameters you have no idea about the
parameters needed for different scenarios.

I rely on type checking in most of my python projects, and even if there is the possibility of typing the
`*args` and `**kwargs`, it looks rather difficult to read.

By having `*args` and `**kwargs` in a function you tell the whole world that the function *accepts everything*.
Its behavior... That is another thing.

For example, see this function that make a HTTP request:

```python
def request(method, url, **kwargs):
    ...
```

Now you need to read the pydoc to know the actual parameters and what do they mean.

By having explicit parameters with type hints, just with a look you can *infer* the behavior of the function.

### Hides the *correct* contract between the two layers
When I see the declaration of a function I do not want (nor usually do I have the time) to read the implementation.
If I am using a third-party library, I do not want to delve into their code. My job is to create software products,
not create software in the void.

I trust the contract that the API libraries provide, and if there are no typed parameters, it is much harder to me
to understand the behavior.

Even in presence of documentation, *code is king*, but we need to keep a balance between reading all the implementation
and only the documentation. I want to read the declaration to make sure that I am calling correctly to the function.
I would rather not need to read (a possibly outdated) documentation.


```python
get(url, json_body={})
```

or

```python
get(url, json={})
```

There is no way to know unless you read the code or the documentation.

### Confuses the LLMs
Without a clear interface, the LLMs are more prone to not have a clear picture of the parameters,
and can *hallucinate*.

### Promotes complexity in functions
It is not a secret that I like simple code and I love linters. I have been playing around with
[pylint](https://www.pylint.org/) and [ruff](https://docs.astral.sh/ruff/)
for several months, and I have come to the conclusion that they are great tools to enforce, not only style,
but *software guidelines*.

Anyway, most linters can limit the number of positional or keyword arguments in functions, hence making it
harder for developers to add many functionality. When I say functionality what I actually mean is responsibilities.
A function should only do one thing and do it well
([Make each program do one thing well in the UNIX philosophy](https://en.wikipedia.org/wiki/Unix_philosophy)).

By passing *everything* to a function we can be falling in the *God function* trap,
where a function does too many things.

```python
get(url, **params)
```

How is *params* used by the function?

### I prefer using keyword arguments all the time
One of things I would usually do is to just use keyword arguments all the time. I know that it is not required, but for me
that makes the communication between the functions more explicit. By doing this there is no discussion about the naming
of the input parameters (as their correspondence to the function arguments is fully mapped).

By using *args, we need to rely on the position of the arguments, and that is error-prone.
Was the URL the first argument? Was the HTTP method? Too much ambiguity.

On the other hand, by using `**kwargs` we encounter other pet peeve: there is no way that we can see if the inputs
we are passing are correct. A simple mistake in the spelling could pass undetected.

```python
get(url, header={'Auth-Token': auth_token})
```

Do you see the error above? It is `headers`, not `header`.

One could argue that tests are the ones have the responsibility or catching issues like this, but unless you are doing
end-to-end tests, and if we do integration and unit tests, we are going to hide this errors.

Would you rather have that or have a *request* function defined like this?:

```python
def request(
    method: Literal['GET', 'POST', 'HEAD'],
    url: str, 
    data: dict[str, Any] | None = None,
    json: dict[str, Any] | None = None,
    headers: dict[str, str] | None = None,
    cookies: dict[str, str] | CookieJar | None = None,
    files: dict[str, FileTuple] | None = None,
    # ...
    ):
```

### It is a solution to a non-problem
I would rather force:

- Keyword-only arguments.
- Make the deprecation of parameters explicit.

than have a custom code that reads from `kwargs` and checks the key name.

### Type hints for *args and **kwargs are not intuitive
No, not only they are not intuitive, it is counter-intuitive, and to be fair I think I have never used type hints in
a `*args` or `**kwargs` before. I have had to read the official documentation to know how to do it:

```python
class Config(TypedDict):
    param1: int
    param2: str


def func(*args: int | str | float, **kwargs: Config):
    ...
```

In no way this is clearer than having the actual arguments with its type hints.
How many positional arguments are? Why not use directly the `param1` and `param2` in the function?

## Conclusion
Avoid using `*args`, `**kwargs`.

Follow [The Zen of Python](https://peps.python.org/pep-0020/): *explicit is better than implicit*.
