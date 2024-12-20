---
title: War stories
date: "2024-12-20T00:00:00+02:00"
draft: false
tags: ["documentation"]
---

# War stories
When talking about software documentation we usually describe the *what* and *how*,
but explaining the reason (*why*) is it left out. Giving a background about why
the team took some decisions can help developers understand better why the software
is the way it is.

## Documentation is a foundational part of software
I would say that nobody doubts that a piece os software without documentation
is not useful. Software can have a big complexity and maintaining it and extend
it can be hard if there is no guide. It would be akin finding the exit from a
maze without a map.

There is a tendency among developers to disregard documentation, in form of
code comments or even in parallel documents. The proponents of this idea
argue that *code is self-explanatory*. Of course, the ones that say this
are the ones that have been working in the same project(s) for years.
I would like to see them struggle to get ahold of a new project of
enough complexity.

## Good documentation is hard to do
Documentation needs to be useful for developers. It must give a big picture and
a background for the project or system it explains.

It also needs to contain architecture, design, technologies, subsystems, etc.
But I am not going to delve in those today.

## Why you should add context
Context gives a lot of information. It can help us understand things better.
From historical decisions to scientific discoveries, knowing the context
is useful.

The context provides some *sand to fill up the cracks* when trying to understand
the mental process of people, so it is needed.

Software is mainly *mental models*, so you can guess the importance of the context
when documenting a complex project. I am not talking about documenting a simple
API, but a project with complex behavior and requirements.

Let me get some concrete examples of issues that context can help solve.
Questions like the following ones are much better understood with context:

- Why did they decide to use this communication mechanism?
- Shouldn't they use this software pattern?
-  What about using this architecture, didn't they know that
it was not going to scale well?

If these questions are not answered properly, or the response is not clear,
the conversation can lead to resentment among creators because they can feel
judged by the new developers.

Most of the time, decisions are limited by the resources of the original team.
So, by giving a background of the context and the restriction the developers
faced, all of these questions can be answered.

## Why should you include concrete examples a.k.a. war stories in documentation
One of the ways the humans learn is *by example*. So, having a a set of
stories in the documentation is even more useful than explaining the context.

Explaining that using Javascript was a decision from the manager or that
a contractor did a sloppy job because he was mismanaged, can be useful for
future developers to understand and, more importantly, empathize with past
developers.

There is no shame in explaining the context (as long as it is the truth),
if there were bad decisions because of bad assumptions, there is no problem
in acknowledging that. Indeed, it is more problematic to defend a bad decision
than to simply explaining that it was taken with the resources that were available
at that time.

## Conclusion
Give some background when documenting software, just describing what it is,
its design and how to use
is not enough. Software design is not a science and
the decisions can better be understood if some
historical context is given, even better if it is done with a *war story*.
