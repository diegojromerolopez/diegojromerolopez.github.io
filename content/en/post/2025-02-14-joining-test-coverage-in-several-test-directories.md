---
title: Joining test coverage in several test directories
date: "2025-02-14T00:00:00+02:00"
draft: false
tags: ["python", "coverage"]
---

# Joining test coverage in several test directories
This post show a simple way of computing the coverage.py's test coverage
in different tests folders.

## Introduction
I have been using
[coverage.py](https://coverage.readthedocs.io/en/latest/) since
I started working with python, and while it works pretty well,
let us say that the interface of the
command line tool could be better.

I struggled for some minutes trying to filter out other folder I have in
my tests folder that were not meant to have their test coverage computed.
Think about some manual tests and other tangential tools.

While I was delving through the documentation, thought about using a
different approach: what about instead of filtering out, adding the coverage
results all together?

## Why would I want this?
Because usually you have different folders for unit, and integration tests.
Some tests are meant to be used for the test coverage, others not.

These are the shell instructions that compute the test coverage for the `tests/unit`
and `tests/integration` folders:

```sh
coverage run -m unittest discover tests/unit
coverage run -m -a unittest discover tests/integration
```

Just by adding the `-a` to the following `coverage run` calls will cause the file `.coverage`
to be extended with the results of those other runs.

Hence, no need to filter the tests by folder or anything like that.

## Why should I worry about test coverage?
Well, that is a discussion for other post, but test coverage gives a hint about
what is being tested or not in a test. Let me explain that a bit. When I am
working on a test (*an actual useful test*) I like to check that the test
is following the workflow that should be.

On other other of things, a good test coverage value also *hints* that at least
the tests fulfill a bare minimum promise of ensuring some checks. However,
there is no guarantee that :

- the tests are actually useful.
- the tests are checking what they need to check.

So, do not trust the test coverage unless you have good quality tests in your
project.

## Conclusion
Split your tests by type, but compute the test coverage in one place!
