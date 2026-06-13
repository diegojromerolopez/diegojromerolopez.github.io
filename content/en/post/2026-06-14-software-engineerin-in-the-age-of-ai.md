---
title: Software Engineering in the age of AI
date: "2026-06-14T00:00:00+02:00"
draft: true
tags: ["llm", "software engineering"]
---

# Software Engineering in the age of AI
Software Engineering has been changing since 2022, now more code than ever is being produced
by leveraging the Large Language Models from AI companies, but does it mean that Software Engineering is in crisis?,
is it going to disappear? Are we engineers going to stop coding?

## Introduction
In this post we are going to talk about how Software Engineering is being impacted by this AI revolution that we are living
now (2022-2026).

## Software Engineering: the two tribes
Almost 20 years ago, when they taught me Software Engineering, there was a conflict among practitioners:
the purists, and the crafters.

The **purists** defended that the code was destined to become a commodity and that the coding process was going to be minimized,
leaving the engineers the high-level design of the system. UML, and other tools where created as a way to have a common language
that allowed the software engineers define their systems fully (or as much as possible) without programming source code.
They were inspired by the other traditional engineers, and considered the code as the building blocks of the system. Some of them
considered that an engineer must not program themselves, but a lower-level technician should do it
(following the engineer directions). Traditional engineers work that way, so they took that approach.

The **crafters** dismissed the efforts of the purists and
considered them *fools* in their own *Ivory tower*, while they were worried about creating functional software by coding it.
They usually did not make a distinction between programming and software engineering.

Of course this is an oversimplification, and most people where had some of each group[^1], but you can get the idea.

In my university days, I was taught by the purists, but soon I discovered, that the world did not needed people that could
create nice diagrams, and documents, but code. The code was the ultimately most valuable piece of the system. The functionality
was in the source code, and indeed one could argue that *the code itself contained the design of the system*[^2].

## Dark Factory
I took notice of this term some weeks ago, meaning a full pipeline where the human is the trigger of the software building process.
A full autonomous process where the human only gives the spec, but they are not involved in the refinement of it. With 
well-configured AI Agents, the *factory* should be able to operate alone, without any other intervention of the engineer.

I have not reach that point yet, but I think that the idea has merit. Of course, the work of a software engineer will be to
orchestrate a bunch of AI Agents that need to analyze and complete the spec, build the software with proper quality, test in
a staging environment, and even release the project.

Anyway, that pattern is what I think that it will become Dark Software Engineering.

## Dark Software Engineering
LLMs are making the generation of code the simplest part of the construction of software projects. Although it was not the
only task of software engineers, a lot of effort was going on programming the instructions to comply with the requirements.
Now, by making use of the LLM technologies, programming is faster and much easier to do[^3].

Following the steps of the Dark Factory, Dark Software Engineering is just a extension. Not only the AI Agents build the software,
but the coding part is mostly hidden from the engineer. The Dark Factory is so-well *oiled*, that the engineer define a Spec,
and the autonomous pipeline should be able to do everything[^4]

### Software Engineering as a traditional engineering
Forgetting about the lowest level aspect of a project reminds me of the purist point of view: the code are the bricks and
can be put by other lower-level technician. Only that this time, it is true. We *steer* the LLM, and it creates a lot of source code.
Source code is not the design anymore, but the specification is. We have come full circle.

Engineers will be liberated from the coding part (for most of the projects[^5])

As with everything in Software Engineering, *it depends*. In case there is no industry regulation or if the consequences of an
error are not dramatical, you can rely on LLMs as much as possible to release the product with a small time to market.

## Conclusion
As my recommendation, start defining a process where ideally you are separated from the code as much as possible. However, keep doing
code reviews and be sure you are *taking the reins* of the LLM by having a good spec and tests.

We need to keep exploring this area, because I predict that the drawbacks will become smaller as time goes by and the LLM models
improve their abilities.

[^1]: Indeed, I consider myself in the two groups. These past years I have given most of my attention to code as the design,
but at the beginning of my career was obsessed with UML, code generation, Model-Driven Architecture, and all kinds of 
standardizations and automatizations.

[^2]: You could say that the code is too low-level to allow you see the design of the system, but the patterns are there.
and there is no way to lie. You can have a mismatch between a diagram and the code.

[^3]: I predict that in 5 years we all have specialized LLMs running locally to help us with the programming of software systems.
There will be cloud models, but the local models would be enough for most people.

[^4]: While I have seen that there are people that do not care about LLMs having to read *tangled* code, I am not at that point yet.
Not to mention, that for some flows (and in some industries or contexts), a human review needs to happen.

[^5]: I am a firm proponent that the human cannot be removed from the creative process, so for some domains in software engineering,
like research, the LLM supports human effort, but cannot replace it ([even when there are some hints that the opposite is true](https://arxiv.org/html/2605.22763v1)).