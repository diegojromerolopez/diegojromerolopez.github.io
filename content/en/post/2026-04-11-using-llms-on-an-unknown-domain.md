---
title: "Using LLMs on an unknown domain"
date: "2026-04-11T00:00:00+02:00"
draft: false
tags: ["llm", "showcase", "golang", "gamedev"]
---

# Using LLMs on an unknown domain

We often hear that Large Language Models (LLMs) empower engineers by augmenting their existing
expertise. But what happens when the engineer is a complete novice in the domain? Can a LLM be more
than just a powerful autocomplete? Can it be a partner when developing for a domain
you have never touched?

## Introduction
I have been "vibe coding" extensively for the last six months. My background is primarily in web
technologies, but I decided to push the limits: build a desktop application in a language I have
*played around* but don't consider my "forte". So I decided to use golang to develop a videogame.

The result is **Oinakos** ([source](https://github.com/diegojromerolopez/oinakos),
[demo](https://diegojromerolopez.github.io/oinakos/index.html)).

## Oinakos: A Dark Medieval Ecosystem

![The first version of the game](/img/2026/04/11/game-01.png)
*The first version of the game*

Oinakos is a Diablo-like isometric action RPG with some RPG elements. While it features traditional
hero progression and combat, it is built on a deep biological simulation. Characters do not just
"exist"; they have metabolic needs (hunger, thirst, fatigue), social relationships, and even
lifecycles involving aging and reproduction.

The atmosphere is a dark medieval world with some Ancient Roman influences. Since I am not an artist,
every single sprite was generated using **Nano Banana 2**, resulting in a uniform aesthetic.

![The version that included the simulation](/img/2026/04/11/game-02.png)
*The first version of the game*

## The Good

### Fast Prototyping
In less than seven days (spending 2–3 hours per night), I had a running game. By strictly prompting, I bypassed the "blank page" syndrome entirely. I reached a functional state remarkably fast—without even reading most of the code the LLM was generating.

### Discovery Process
Instead of searching for how to deal with the images, or collision algorithms, I just asked the LLM to
present me with different alternatives. Sometimes the alternatives were not what I was looking for,
but those even worked as a baseline. I asked the LLM to search for a good game engine for Golang, and
it suggested [Ebiten](https://ebitengine.org/).
I did not have to worry about choosing the graphics library!

### AI-Driven Intelligence
One of the most exciting aspects of Oinakos is its integration with modern AI providers.
Whether in the **live GUI mode or the headless simulation**, characters can be controlled
by **OpenAI, Claude, Gemini, or Hugging Face**.
By leveraging these AI LLMs, the characters move beyond simple script-based behaviors,
they make decisions based on the current world state, their metabolic needs, and their relationships.
This creates an emergent "living" world where the players can witness complex interactions that weren't explicitly hard-coded,
effectively turning the game into a sandbox for biological and social AI experiments.

![The settings](/img/2026/04/11/settings.png)

### No Domain Gate-keeping
You do not need to know your domain perfectly to start. You need foundations,
but the LLM removes the "gate-keeping" of syntax and specific engine quirks.
I let the LLM do the exploration for me, discovering choices and trade-offs in gamedev
that I otherwise would have had to spend weeks researching.

### All the chores done for me
The boring implementations—distribution for several operative systems, GitHub Actions pipelines,
boilerplate test files were all handled for me. I could focus on the "fun" part of the game logic
while the LLM did the literal heavy lifting of the initial setup.

![The GitHub pipelines running](/img/2026/04/11/pipeline-running.png)

## The Bad

### Context Size Limits
Oinakos ended up with 300+ Go source files and over 35,000 lines of code.
It is impossible to feed the entire codebase into an LLM's context.
You have to learn to provide "pointers" and specific file subsets,
or the model starts losing the thread of the architecture.

### Output Size Constraints
After some months of work, I started seeing stalls in the responses.
I suspect that because of the massive logs and complex outputs,
the service triggered failsafes that cut the response short.

![The first version of the log](/img/2026/04/11/log-01.png)
*The log system was paramount for LLM-game communication.*

### Hard Problems are not Resolvable (Automatically)
I asked the LLM to speed up the simulation twofold by leveraging goroutines.
It implemented a solution that looked plausible but was a total disaster.
Because I had not explicitly audited shared resources, the code was riddled with race conditions.
The LLM will not always warn you that a solution is dangerous, it will simply produce a plausible-looking failure.

### Context/Project Rot
Without the full codebase in view, LLMs start making "greedy" choices: modifying parts of the code outside the current scope or
breaking existing patterns. I had to enforce a rule: every change must be covered by a test.
This slowed the "vibe," but it was the only way to ensure the project didn't collapse under its own weight.

### The Graphics Feedback Gap
Adjusting a UI through text is like painting with your eyes closed.
Descriptive prompts like "make this box shorter" aren't enough when you can't see the result.
While the LLM tried to run a WebAssembly instance and use the Chrome inspector to "see" the UI,
the process was painfully slow.

## The Ugly

### Quota and Model Choice
I was often forced to use faster models due to quota issues with Pro models. This lead to a noticeable drop in structured logic. Using the right model for the right task is paramount, but when the quota runs out, the "vibe" slows down significantly.

![My quota was always run out](/img/2026/04/11/quota-run-out.png)
*Managing quotas became a project in itself.*

### Plan First, Execute Second
As the project grew, I had to stop "vibing" and start planning. I ended up with dozens of markdown plans where I had to check the logic myself before execution. We cannot expect an LLM to read our minds in an ambiguous, 35k-line environment.

### The Project Asymptote
The "Project Asymptote" is the feeling that as the codebase grows, the effort to reach 100% completion increases exponentially.
The model starts tripping over its own past decisions until you take control back as the Lead Architect.

## Conclusion
Building Oinakos proved that while LLMs remove the gate-keeping of syntax and domain knowledge,
they heighten the importance of **Systems Design**.
You can build a large engine without being a professional expert in that specific language,
provided you have the discipline to enforce architectural rules and rigorous testing. 

The gate is open; just make sure you know the fundamentals.
