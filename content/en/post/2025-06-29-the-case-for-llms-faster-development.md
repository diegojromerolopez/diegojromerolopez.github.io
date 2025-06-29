---
title: "The case for LLMs: faster development"
date: "2025-06-29T00:00:00+02:00"
draft: false
tags: ["software", "ai", "llm"]
---

# The case for LLMs: faster development

## Introduction
Artificial Intelligence is all over the place in software development these days.
From the first AI services that could generate images, to the code generation tools
like GitHub Copilot, ChatGPT, Google Gemini, etc.

I wrote in [other post](/blog/2025/05/can-llms-replace-engineers/) that LLMs are not going to
replace software engineers, but they are going to empower them in a lot of cases.

This post is a *war story* of mine, where I used a LLM service to create a new command
for a CLI command tool written in a compiled language that I do not *master*. I know how
to read some code, but I am not skilled in the ecosystem nor in many patterns and conventions
of the community.

## The war story
**I needed to develop a new command for a CLI tool** where I lack of meaningful experience with
the programming language, the main library or the ecosystem.

Most readers will remember that I am very fond of the Python programming language, while I have
worked with Ruby, and TypeScript lately. Anyway, in this case the programming language was none
of those, and I wanted to spend the less time possible creating it.

## Teachings

### You need to know the tool a little
I already knew the language, I learned it in 2020 via online courses, and I did an open source project
to improve my skills (*you cannot learn to program without programming*). I like the language and saw
(and I see) a lot of potential in it.

I was not a novice with the *tool*, but I was not used to work everyday with it.

**You need to be able to read and understand the code the LLM is generating**.
You cannot ask a LLM to create code in Rust while you do not understand how memory management works in such
a language. You cannot ask LLM to create an async function when you do not understand what an async function is.
You cannot create a threaded code while you do not know what a critical section is.

### You need to know the foundations well
I am a senior engineer, I know how this kind of applications work. I know the perks of the language, and I
consider myself skilled enough to do a good work in my language of choice, it is not the needed one.

**When you work with LLMs you should know the issues that can rise from the code you are generating**
(e.g. concurrency, i/o, bottlenecks, algorithmic order, performance...).

### You need to know the task well
I knew how to do the task in hand in other languages, but not in the one I needed to do it.
Indeed I had implemented it in Python, so I was very knowledgeable of the functionality that I needed
to develop.

I knew that I could do the explanation (*the prompt*) in a way that the LLM could understand me,
giving examples and making it clear the different workflows that needed to be implemented.

You need to be persistent when explaining things to a LLM. If there is some room for ambiguity, the result
will not be the one that you expect. **Be as explicit as you can**.

### Know your surroundings
Before I asked the LLM to create the code, I read some of the commands that were already implemented there.
I have not worked with the library that the maintainers chose, so I tried to extract some patterns about how
a new command is defined, how parameters are defined, etc.

Once I had a good idea about how it worked, I then created the prompt and gave some draft about how the command
should be. I did not started from nothing, or just plain language. I game the LLM something to work on, to fix,
to improve, to build on.

When working with LLMs, **provide a code draft the LLM can base its work on**.

### LLMs commit mistakes
The LLM that I was using did several important errors while generating the code.
Indeed these errors were so big that were making the program to crash and not fulfill its
mission.

I needed to review the code and ask it to fix the part that was the culprit, explaining to the
AI what was the condition that was wrong.

I did not know exactly the name of the function that I needed to call to solve the issue, but I knew
what had to do, so I explained it to it.

So, no, **LLMs are not perfect and their code has errors**.

### Be demanding with the LLMs work
Once I had the code running, I asked the LLM to create some tests for a function, and one of tests
it was a myriad of smaller tests in a loop. I did not like that.

I asked the LLM to split the test in several smaller tests (as it should be), and I could select the
actual tests that had some sense, and discard the rest.

**Do not accept code as-is from the LLM. You need to review it and judge as if it was a junior team mate**. 

### You need to do manual changes
You cannot spend all the day just asking the LLM to fix issues. Because every time you ask for a new version
of the code with a fix, you risk having new breaking changes being introduced in your code.

While I know there is some *vibe coders* that like to work with the LLMs modifying all the project code, that is not
my case: I would rather give some smaller context to the LLM to help it fix it, or just fix the issues by hand.

Be ready to fix some small issues by hand. **Do not fall in the trap of having a back-and-forth conversation with the LLM**.

### LLMs help you work much faster
Of course I had the code up and ready in less time that I would have spent by coding everything by hand.

Overall, it was a fruitful and pleasant experience.

### Beware of generating too many lines of code
But as all the pleasant things, it is better taken in moderation.

If you generate a lot of lines of code, you cannot expect the reviewers to read as fast as a LLM.

Unless you trust a LLM to review your code, you will need to first review the code yourself, and then
create the functionality in chunks that are easily reviewable.
**Nobody likes to review pull requests with 500 changes**.

## Conclusion
LLMs are powerful tools but need to be driven by a skilled engineer.
They are fallible and can create tangled code easily.
**The LLMs need to be under human control always**.
