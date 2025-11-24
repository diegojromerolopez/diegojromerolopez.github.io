---
title: Use LLMs to handle tedious tasks
date: "2025-11-24T00:00:00+02:00"
draft: false
tags: ["llm", "ai", "war-story"]
---

# Use LLMs to handle tedious tasks
There are some times where there are tedious tasks that need to be done in our software projects.
We know how to do it but usually delay them because they are boring, 
not challenging and painfully long. The LLMs (Large Language Models) promise faster 
and better software development.
Could we use a LLM to do them? Could we leverage the LLMs to free them from these chores?

## The problem
I wanted to fix the type hints of my [Gelidum](https://github.com/diegojromerolopez/gelidum) project.

I create this library for freezing objects in Python and when I did it I did not check the
type hints with [mypy](https://mypy-lang.org/). Time passed and I keep on adding new features,
but the type hints were not correct, and the errors starting piling up.

Some months ago, I run mypy against the project, and the number of errors was of almost 1 thousand.

## The tool
I used the [Antigravity IDE from Google](https://antigravity.google/) because they provide
a beta version with full access to LLMs. This IDE also has a conversational agent mode, where
the agent asks you for your feedback in each step.

## The solution
I opened gelidum in Antigravity and started asking questions to *Claude Sonnet 4.5* with the *plan*
conversation mode.

The first solution was a raw one, it offered me to ignore the tests completely and improve the current
status of the type hint by fixing issues in the code.

The AI removed some code from the library, and I needed to revert that change. It thought that I
was not using the set operations, but I was indeed using them and the test crashed!

After some back and forth, I also told it to use generic types,
it did what I want it to do: use the Frozen generic type.

Apart from that, I ordered to not ignore the tests, *et voilà* I had some Python code with type hints.

Of course, there was some manual fixes done here and there, and my directions to the LLM, but the
*boring and long* part was done by the LLM.

I created [a merge request](https://github.com/diegojromerolopez/gelidum/pull/50)
and started applying some other manual changes to the code.

## The lesson
You need act as the navigator of the LLM because it lacks agency to know if the solution
is the optimal one of a local optima.

You cannot blindly rely on what the LLM tells you. Most of the time the LLM is going to give you
the easiest solution possible, even if it implies removing non-functioning code, instead of
fixing it.

## The benefit
A task that I was postponing for months done in just a couple of hours and a LLM.

## Conclusion
Use LLMs for easing the pain points of software development.

Do not trust the generated code by LLMs. They are lazy and will fall in local optima.

Know the fundamentals. The LLM follow your lead. If you do not know 