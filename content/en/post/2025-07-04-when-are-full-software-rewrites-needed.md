---
title: When are full software rewrites needed?
date: "2025-07-04T00:00:00+02:00"
draft: false
tags: ["software", "practices"]
---

# When are full software rewrites needed?
Having dealt with a full rewrite of a software application recently, it left me
wondering if it was needed at all, if there was any way to salvage the project or
some parts of the project. Could we have avoided the rewrite?

## Introduction
There was a time where I had to maintain and extend a deprecated project, until the deadline came.
I was upset because it was a failure of management to not be able to predict this outcome, and I was
the one that was ordered to create the replacement. The migration was a success, I was burned out
and (maybe because of that), a bit disappointed about having to retire the original project, but there
was no alternative as our provider had sunsetted the functionality our main dependency was based on.

I remember another case of these rewrites. In this case, it was a a project that was a simple pipeline job
aggregator was implemented by an engineer in a programming language that was not common for backend services,
and they decided to use domain-driven design with CQRS as the design of the application.

For an application that just have a simple backend service that needed to:

1. Receive a HTTP post with some job information and store in a database.
2. Read the database and give job information based on some filters.

It was a very bad decision, a way to increment the artificial complexity by 10x.

So, after having done two full rewrites of applications. Is there any way to avoid this (in a way) wasted effort?
Why do I feel that the projects were rushed and no consideration were taken with respect to maintenance?

## Things to take in account when considering rewriting a software project:

### Projects die
But software is a continuum. Software *rots* and needs to be replaced continuously. Unless your software lives
in a vacuum and has been mathematically proven to be perfect, you would need to maintain it and create new
features.

### Try not do, but if impossible do it
Doing a full rewrite of a software project is less than ideal. It is like paying twice for a thing, like a lot
of wasted time. However, sometimes there is no way to get around them and they are totally needed.

### Full rewrites are born from bad past-decisions (Mostly)
If the cost of adding new features or maintaining the current piece of software is going to grow along the years,
maybe investing time in a full rewrite is a good decision; a good way to avoid the *sunken cost fallacy*.

But what is a bad past-decision? Mainly just creating artificial complexity in the project.

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
Following with the example of the job aggregator, why did they decide to use a programming language focused in mobile app development as
a backend language? There are a lot programming languages more popular, and easier to work with that this one.
Maybe they wanted to learn a new language? I would not want to guess their thinking with this respect.

Anyway, try to use a tool that provides you with the most functionality for what tha aim of the application is,
the most supported ecosystem, libraries, and the biggest community.

What would you choose?

1. The most used programming language (Python) or one that is cool and you want to learn?
2. An official library or one done by a lone developer?
3. A library that uses a pattern that provides a 5% of performance gains or the standard way of doing things?

## Conclusion
Always consider the alternative when pondering a software rewrite, but if not possible, rewrite.

Always create software the most durable possible by basing your project in popular, usable, easy, and the right tools.
