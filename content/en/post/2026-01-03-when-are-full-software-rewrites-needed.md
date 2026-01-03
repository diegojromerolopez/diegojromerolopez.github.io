---
title: When are full software rewrites needed?
date: "2026-01-03T00:00:00+02:00"
draft: false
tags: ["software", "practices", "tech-debt", "war-story"]
---

# When are full software rewrites needed?
Having dealt with a full rewrite of a software application recently, it left me
wondering if it was needed at all, if there was any way to salvage the project or
some parts of the project. Could we have avoided the rewrite?

## Introduction
I have encountered the necessity of rewriting full software projects several times
in my career but in my last years I have had to do it twice.

I think that a full software rewrite is a failure (in a way), and an opportunity.

A failure because if a rewrite is needed, the software was not engineered, but simply created in such a way
that there was no improvement possible.

An opportunity because we can learn from the previous project and not commit the same mistakes.

## Some war stories about rewriting software

### Story 1: The deprecated bot
There was a time where I had to maintain and extend a deprecated project (a ChatOps bot).
I warned my manager but I was ignored; and then, the deadline came.

I was the one that was ordered to create the replacement. The migration was a success, I was burned out
and (maybe because of that), a bit disappointed about having to retire the original project, but there
was no alternative as our provider had sunsetted the functionality our main dependency was based on.

### Story 2: The job API

I remember another case of these rewrites. In this case, it was a a project that was a simple pipeline job
aggregator was implemented by an engineer in a programming language that was not common for backend services,
and they decided to use DDD ([domain-driven design](https://en.wikipedia.org/wiki/Domain-driven_design))
with [CQRS](https://en.wikipedia.org/wiki/Command_Query_Responsibility_Segregation)
as the design of the application.

For an application that just have a simple backend service that needed to:

1. Receive a HTTP post with some job information and store in a database.
2. Read the database and give job information based on some filters.

That decision was unfortunate, as it incremented the artificial complexity by a large margin.

I am not against DDD at all, I love that it provides a common language for software engineers
and the patterns they bring with it (repository, services or domain objects are great!).
However, it introduces a lot of complexity, that most developers are not
familiar with, and that can derail the maintainability of the project.

## Things to take in account when considering rewriting a software project

So, after having done two full rewrites of applications. Is there any way to avoid this (in a way)
wasted effort? Why do I feel that the projects were rushed and no consideration were taken with
respect to maintenance?

### Projects die
But software is a continuum. Software *rots* and needs to be replaced, and improved continuously.
Unless your software lives in a vacuum and has been mathematically proven to be correct,
you would need to maintain it and create new features.

### Try not do, but if impossible do it
Doing a full rewrite of a software project is less than ideal. It is like paying twice for a thing,
it feels a lot of wasted time. However, sometimes there is no way to get around them and they are totally needed.

### Learn from your mistakes
Given that a rewrite should be a last-resort measure, try to leverage the knowledge you got from working with the
old code base to learn what went wrong. Is it the design? The artificial complexity that it entailed? The choice of the tools?

Make the most of the rewrite. If you do it, make sure that the project is ready for onboarding new people in the
easiest way possible.

### Projects need to be self-contained
You should not need any external knowledge to build the project apart from the basics of the language and framework.
Even, those should be documented.

The project should have clear instructions about how to work with it:

- Architecture.
- Conventions.
- How to collaborate.
- How to run it locally.
- How to run the tests.
- How to extend it.

Recently I have started working in a project where there was no instruction about how to run it locally.
That is not acceptable.

### Full rewrites are born from bad past-decisions (Mostly)
If the cost of adding new features or maintaining the current piece of software is going to grow along the years,
maybe investing time in a full rewrite is a good decision; a good way to avoid the *sunken cost fallacy*.

But what is a bad past-decision? Mainly just creating **artificial complexity** in the project.

A unmaintainable project, well because of a bad architectural design, or a bad programming language, or a bad libraries
can make taken de decision of the rewrite the best course.

### Full rewrites are born from maintenance not being a requirement
In this world, having a fast time to market is encouraged, maintainability takes a second (if not the last) position.
The popular concept of tech-debt can make projects impossible to extend, or even worse, fix in any way.

Now that the LLMs are being used by myriads of people to develop software as fast as possible,
I wonder *who is going to maintain that*.

Maintainability is a must, is a requirement always. I am not asking for discussing every decision with the team an reaching
agreements about the best way to do it. I understand that some times functionality takes precedence over quality. However,
it cannot happen in all the project. Following good practices is not asking for the impossible, and quality should always be
taken in account.

Good software patterns, complexity and coupling measurements, and testing coverage are some of the tools that need always to be used.

### Avoid rewrites by using the better tool for the job
Following with the example of the job aggregator, why did they decide to use a
programming language focused in mobile app development as a backend language?
There are a lot programming languages more popular, and easier to work with that this one.
Maybe they wanted to learn a new language? I would not want to guess their thinking with this respect.

Anyway, try to use a tool that provides you with the most functionality for what tha aim of the application is,
the most supported ecosystem, libraries, and the biggest community.

What would you choose?

1. The most used programming language (Python) or one that is cool and you want to learn?
2. An official library or one done by a lone developer?
3. A library that uses a pattern that provides a 5% of performance gains or the standard way of doing things?

## Conclusion
Always consider the alternative when pondering a software rewrite, but if not possible, learn from the mistakes
and rewrite the project.

Your job as an engineer is to make the project the easiest to understand, and work with for everybody.
**Think about others when developing software**.

Always create software the most durable possible by basing it in popular, usable, easy, and the right tools.
