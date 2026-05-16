---
title: "LLM mental fatigue"
date: "2026-05-17T00:00:00+02:00"
draft: false
tags: ["llm"]
---

# LLM mental fatigue
LLMs (Large Language Models) provide a wonderful tool for the construction of software
that speed up the process of coding. But are there some downsides to them?

## Introduction
The past 3 years have been a total change in the software engineering discipline,
first the AI-based autocomplete, then the LLM-based code generation. 
Now, non-software engineers are creating and releasing software *in the wild*, and
software engineers are being pressured to produce software faster.

We know the benefits: automatic generation of *scaffolding* code, faster proof of concept building, etc.
Ultimately, **faster delivery of software**.

## What some studies say?
Using LLMs *tires the mind*, if we had a coding speed before using this technology,
now the speed is 2x or even 4x times faster. We need to create, review, and assess
the generated code. This creates an imbalance, and forces the developer to focus and
work with a much greater speed than they were used to.

Since I have been working with LLMs, I have felt that having to *babysit* the LLM
constantly is difficult, but having to review all generated code (at the speed the LLM generates it),
is even harder. This extra-work fatigues the mind and m

I am not alone in this sentiment, in Feb 2026, *Aruna Ranganathan* and *Xingqi Maggie Ye* wrote
about this phenomenon
([AI Doesn’t Reduce Work—It Intensifies It](https://hbr.org/2026/02/ai-doesnt-reduce-work-it-intensifies-it)),
and there was an interesting
[discussion in Hacker Hews](https://news.ycombinator.com/item?id=46945755) about this.

In an [interview with her Alma Mater, UC Berkeley Haas](https://newsroom.haas.berkeley.edu/ai-promised-to-free-up-workers-time-uc-berkeley-haas-researchers-found-the-opposite/),
Xinggi Maggie Ye said something that resonated with me:

> [The AI background processes] created a rhythm where both the human and the machine were constantly in motion.

Steve Yegge advocates for [reducing the work hours for the developers that use LLMs to 3 hours a day](https://newsletter.pragmaticengineer.com/p/steve-yegge-on-ai-agents-and-the),
because of this mental fatigue. For companies to allow this, we should all change our mindset as society,
and seen the *return-to-office* policies lately, I do not think we are ready for that.

## My experience
LLMs are great in helping you develop faster, and better software. Faster because you can design a spec, and the
LLM will make its best to create code that fulfills it. Better because you can set up guardrails for the LLM to
follow principles of software engineering when creating the code. There are some caveats, though.

### The excitement

When I started working with Claude Code, and Antigravity,
I felt as a shepherd of a stubborn, *dumb*, giant sheep. The LLM had to be guided step by step, and I improved
my skills in a way that I was able to be almost 5-10 times more productive that I was without using AI.

However, when dealing with the LLM, I discovered that I had to be extremely vigilant, because the result would not
have enough quality. Deprecated code, code that avoid edge cases, or simply hallucinations that, while they
were syntactically correct, did not work. Even worse than having non-working code, it was ending up with a code
that was unmaintainable but apparently correct: new undesired dependencies, repeated code,
code without encapsulation, code that had no separation in layers or anything, code that followed no software engineering guideline ever. Ultimately, code that could not be understood unless a considerable effort was done. 

### The harness cycle

To avoid generating code that no human could maintain, I enforced a feedback loop with linters, tests, and software
engineering guidelines ([Domain Driven Design](https://en.wikipedia.org/wiki/Domain-driven_design) and
[SOLID](https://en.wikipedia.org/wiki/SOLID)), to at least have a minimum quality.

One of the most important parts of this harness is to have a strong collection of tests, mostly integration tests.
I wrote about that in the post: [creating a complex project with LLMS](/blog/2026/02/creating-a-complex-project-with-llms/).

I also enforced maximum size of generated files (a *raw* way of ensuring a minimal encapsulation),
and asked the LLMs to not fall in the trap of the "god" objects.

I perfected this harness and eventually reached to a point where the code was "good enough".

### The fatigue

But the problem is not that the LLMs . The problem is that you do not have a chance to disconnect.
I started feeling that I was focused all day, and that started to mentally tire me. After a workday
I felt tired, unable to read, or have a meaningful conversation.

My role changed completely: from creating software, to supervising agents creating software.
The pace of the LLMs is much faster than your typical human, so I started becoming
the bottleneck of the pipeline.

Apart from being on the flow all day, the stress of consuming too much tokens, or the auto-exigence
of having the perfect plan, with the perfect prompt, and to understand the generated code,
was making me *a bit* anxious all the time.

### The realization

The LLMs are a powerful tool, but **we cannot force us to work at the same speed as them**.
We need *to be at the wheel* at all times, and ensure the code not only does not have bugs,
but it does what it needs to do.

The *human* needs to be aware of the architecture, the design, and the patterns in the code.
A software engineer cannot be a passive agent when developing software, they need to enforce
a standards in quality, and maintainability. We cannot afford to have a software that works
but it is brittle, cannot scale, cannot be improved or extended, and the worst of all,
nobody understands it.

Not always fast means better.

## Conclusion

LLMs accelerate the creation and shipping of software.

Do not try to follow the pace of the LLMs. That can lead to mental fatigue and burnout.
It is more important to have a control of the code generation, than creating lots of code that cannot
be understood.

Software Engineering is becoming a discipline where the coding part is less important than supervising
AI agents creating code.