---
title: Don't touch that
date: "2023-10-12T00:00:00+02:00"
draft: false
tags: ["legacy", "code", "software"]
---

# Don't touch that
Have you ever been told "don't touch that, if you modify that piece
of code you are going to break anything"? How did you react to this
comment? Did you feel "attacked" or simply ignored that piece of *advice*?

## Code jungle
Starting a working on a project that has some *dark corners* is a
daunting task but following some guidelines can be useful.

## Scary code
There is always some *scary code*, I do not mean code that is difficult
to understand, but code that has unintended consequences if modified.
Code that if it is changed in order, breaks something. Of course the code
has no tests at all, or even worse, the tests do not help with detecting
errors.

Usually this code has been created "organically", and by that I mean
chaotically, i.e. without any kind of software design. Global state,
no documentation (because of clean code) and no useful tests, because
"we mock everything".

This kind of code works but modifying that could cause an outage easily,
as even the minor modification could cause an service failure of gigantic
proportions.

## The cursed phrases
And now is when phrases like *This is too difficult*, *Don't do that*,
*Do not modify this code* enter the room. Maybe you are a new employee
and have no experience dealing with the project but... I cannot help
to feel a bit of *contempt* when listening to that. Of course that is
only a perception and not the true intent of the person I am talking to,
but being told "you are not experienced to to something" *stings*.

## The cursed state of things
Of course a job it is just a job, we should not care about this kind
of non-sense, and work everyday, providing value to the company we work for.
However, do this kind of disarray, this untouchable code, unknown
behaviour in projects provide value to the company?
I do not think so. Providing value to the company is also ensuring
you can *continue providing value to the company* in the future.
We are not working in some stone-sculpted monument, we work in a
dynamic, changing, and inmaterial environment and means. There should
not be untouchable code.

## What to do
There is a good book (maybe a bit dated) called
[Working Effectively with Legacy Code](https://www.oreilly.com/library/view/working-effectively-with/0131177052/)
that gives some good pointers to deal with this. It is almost 20 years old,
but it gives advice on how to tame the beast that is legacy code.

The most important lesson the book contains, I would say, is ensuring you
have the main workflows covered by tests before doing any change. So, once
you start working on refactoring pieces of code you do not break anything.

Of course, tests need to be actual tests, not the kind where you mock
everything and that is all. In this case, I would vouch for integration
and end-to-end tests.

I wrote a post some time ago about my idea of how the tests should be.
[Take a look at it](/blog/2022/11/actual-integration-tests/).

## Conclusion
Ensure no code is untouchable by having actual tests that leave no
flow untested. Once you have that, refactor the code to make it
understandable, and extensible.
