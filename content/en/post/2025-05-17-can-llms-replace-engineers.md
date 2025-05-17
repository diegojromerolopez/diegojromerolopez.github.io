---
title: Can LLMs replace engineers?
date: "2025-05-17T00:00:00+02:00"
draft: false
tags: ["software", "ai", "llm"]
---

# Can LLMs replace engineers?
This post provides my opinion about how a [LLMs](https://en.wikipedia.org/wiki/Large_language_model)
cannot replace a senior software engineer,
even if the CEOs and other executives believe that it is possible.

## Introduction
I have been using Artificial Intelligence (in the form of LLMs) for several years already.
My experience working with LLMs is limited to working with [ChatGPT](https://chatgpt.com/),
[Cursor](https://www.cursor.com/) and [GitHub Copilot](https://github.com/features/copilot)
as of May 2025 (when this post was written). So please, if you read this in the future,
take my opinion with *a grain of salt*.

Maybe, you do not know but there was a time were I studied Neural Networks and even considered
the academic route by enrolling in a PhD. programme in this field.

Of course, *life finds a way* and I ended up in the square 1, i.e. Software Engineering, but that is a story
for another day.

## What are LLMs?
I am in no way an AI expert, but let me explain succinctly what LLMs are.

Large Language Models are a kind of Neural Networks that have billions of parameters (hence the *large* adjective),
and are trained with all the knowledge of the internet. So they mimic (in a way) the human reasoning. That is why
they are being classified as Artificial Intelligence, term that I dislike particularly because it suffers from
inexactitude and being a marketing-loaded term.

## How do they work?
I am not going to explain the technical details about how they work here, 
but I think that a good metaphor can be useful for people to understand the foundation of the tool.

Basically, the LLMs create sequence of texts where every word is the best match (based on the previous words).
I like to think of the LLMs as Extremely High-Powered Markov Models. Of course, Markov Models are not more than
a plaything compared with the LLMs, as they stablish more complex relationships between information, they have
a number of parameters that is enormous, and they are compressed. They do not need to have a conditional probability
table for each term, the LLMs store this relationships with the Neural Network weights.

Of course current state-of-the-art LLMs have memory and a lot of techniques that are very advanced, but
we can ignore those and just keep thinking about them as *Parrot Machines*.

## How I use them?
I have several use cases where I make use of the LLMs everyday, let's check them out:

### Product ideation
I am currently a senior member of the Engineering Productivity team, so apart from my software development
duties I also act as a product owner of several projects.

I use LLMs as a way to get ideas of new features that could be implemented. Those features of course are polished,
first by me, later I ask for internal and external feedback, but the seminal idea can come from whatever place,
include a LLM.

Most of the ideas are *recycled* ideas from other places or could be *low-hanging fruit*, but nonetheless, they are 
useful. There is always some new piece of information that can be useful.

### Merge request reviews
I think that for mistakes and simple errors a LLM can provide value. Of course, it is not going
to get all the context and understand the state machine of your software, but for forgotten variables,
missing returns, or inconsistent states, it can work.

Think of this as a *high-order linter*.

### Pair programming
While the LLMs do not have the same ability than us humans, they can be pretty useful for discussing
technical details with them, improving our overall performance.

For example, let me bring an example where I used a LLM to optimize a service that depended on a sequence
of HTTP requests that could not be parallelized, because each request had a dependency with the previous one.
Well, I did not notice that I was not sharing the HTTP session among the requests, so I was inadvertently adding
some milliseconds to each loop.

So, in a way the LLMs can be a good solution for getting a better solution because of these simple mistakes.

### Chore programming tasks
Defining a TypedDict or a database schema is a chore. Usually I just paste some example data in the
chat and ask the bot to create the code for me. Surprisingly, it works pretty well.

When there is no room for error, no ambiguity, and the example is clear the LLMs excel.

However, you need to keep being specific and meticulous when defining the task. For example,
the generated TypedDict usually uses only strings, and not string literals. I love having literals type hints
in my python code as they are very explicit about what they are (can it be more specific than saying
*I expect this variable to have this built-in value?*).

### Prototyping
Sometimes I find myself daydreaming about how can I implement this feature or this programming language
has the ability to do this in this way or the other...

I think the last one I asked this kind of question to ChatGPT was when I wonder if there was any way
of doing static range checks to integers in Python (not really, although you can use
[Annotated](https://docs.python.org/3/library/typing.html#typing.Annotated)).

It is fast to prototype a functionality or check if it is possible via a LLM, however the ground work
needs to be done by you, because you are the one that has all the context and have the information
about what you actually want to do.

### Natural language style check
I just wrote *How I do not use them* when writing the title of this sub-section. I thought
it *sounded wrong* and I asked ChatGPT, only to be confirmed that it is indeed an archaic
sentence.

The point here is that English is not my mother tongue, and I get myself lost in the idiosyncrasies
of the English language. Differences between the American and British spelling, avoiding colloquialisms,
or being rude are some of the aims I have when checking my English with the LLMs.

### More intelligent auto-completion
I think this use case is the most popular one among the software developers. Using GitHub Copilot
to have the IDE auto-complete your sentences is useful.

However, I think there is a lot of potential for errors, because of the hallucinations of the models
(as of May 2025). There has been a good amount of instances where the suggestion made no sense at all.
It is good for trivial and repetitive chunks of code
([OTEL span](https://opentelemetry.io/docs/concepts/signals/traces/#spans) attributes, for example).

### Bonus: diagram repair
This is a small one but I found the AI diagram fix in [mermaid](https://mermaid.js.org/) pretty useful.
I used it recently to fix a broken diagram
because I didn't want to read the syntax documentation (I should have).

## How I don't use them?
When the LLMs do not excel? I have encountered several scenarios where their performance is... disappointing:

### Full project generation
The amount of effort I need to use to explain myself to the LLM to create complex projects is not
worth it when I can be faster coding it myself.

### Non-popular/Rapidly evolving technologies
When I was doing a microservice in [deno](https://deno.com/) I was finding myself at loss many times.
How to use open telemetry, how to create a middleware in [deno fresh](https://fresh.deno.dev/), etc.

The problem is that deno (and fresh) have been changing so much that asking ChatGPT for guidance
is a recipe for getting misleading (and non-functional) code. The LLM have been learning with
code that is no longer correct, so it suggested wrong ways of doing things. The worst part
was feeling like a reviewer of the LLM code and trying to convince it that the code was deprecated
(or even removed), hence making it incorrect.

At the end of the day, I searched actual deno projects and read the documentation. So,
**do not think you can avoid reading the docs by using LLMs**.

### Code Refactoring
Mainly I have used Cursor and GitHub Copilot for this, with several models (ChatGPT among them)
and the results have had less quality than what I expected.

I have the theory that the current LLMs are not able to hold contexts that are big. By big I mean
information about more than 20 implicit states, for example. I have tried to refactor a piece of
code where there was a lot states with indirect dependencies and the result was not useful at all.

I am not saying that a human could have done it better, but in my experience only small function-level
refactors can be done based on LLMs.

I hope this improves in the future, well I am sure it will.

## Conclusion
While the LLMs are a great tool and you should be using them, do not trust them to be
the ultimate tool to solve **all** your problems.
