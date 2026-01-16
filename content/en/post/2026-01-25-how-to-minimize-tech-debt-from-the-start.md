---
title: How to minimize tech debt from the start
date: "2026-01-25T00:00:00+02:00"
draft: true
tags: ["software", "tech-debt"]
---

# How to minimize tech debt from the start
In this post we are going to lay some guidelines about how to prevent your project of accumulating tech debt.

## Introduction
Tech debt has been a constant in all my work. All projects I have started working with had an amount of tech debt.
Why does this happen? And better yet, what can we do to avoid falling on this tech debt trap?

## What is tech debt?
[Tech debt](https://en.wikipedia.org/wiki/Technical_debt) was a metaphor created by
[Ward Cunningham](https://en.wikipedia.org/wiki/Ward_Cunningham) to help non-technical people
the necessity of investing resources in keeping the software projects with the lesser level of accidental complexity possible.

There are several types of complexity in the software world, **inherent complexity** comes from the functionality that is
implemented in the software, while **accidental complexity** refers to parts of the project that are as simple as they could be.
So assuming the perfect code that solves the problem, accidental complexity is all the decisions that derail the project in other
direction. Things like no encapsulation, god objects, no abstraction, coupling, etc. can make the project difficult to understand.

Apart from this complexity, **software is always evolving**, libraries and runtimes are upgraded and change, and the projects
that use them need to be adapted. Not doing this can be risk and even threatens the business continuity. A software project
with outdated dependencies is at risk of being attacked by a malicious entity that leverages a security vulnerability.
Or you can find yourself without a functionality because the outdated dependency does not work anymore.

Another important aspect of software is that it is difficult. While a lot of people think that it is just a matter or
writing some code doing one thing, once the software project starts growing so many different combinations of statuses, flags,
settings and internal states that it is not tractable. That is called indeed the state explosion problem.[^1]

Of course, the tech debt term could be considered subjective, but we have a lot of ways of measuring the accidental complexity,
and it is easy to check the project dependency versions. Nowadays, there is less room for debate about what is actually
tech debt and what it is not.

## How projects grow in tech debt?

### By going too fast

Mainly by cutting corners during development. As the market pressure mounts up, the software engineers/developers feel pressured
to release the features early. That means, less tests, worse designs, not relying on software patterns, and not applying decades
of empirical evidence when developing the project.

### By using AI wrongly

Now that the [vibe-coding](https://en.wikipedia.org/wiki/Vibe_coding) is popular,
I see a lot of people doing showcases of software projects done by non-developers.
They show a *flashy* interface and some functionality that works fine. However, let me tell you a secret: this does not scale.
Once you want to productize the project, the *tangled mess* that is the code[^2] is impossible to deal with. That is why it is so
important to give directions, and review what the LLMs are doing when we ask them to work for us.

### Consequences

The PM (product managers) are happy because the developers release faster, but they are not aware about
the *sweeping below the rug* that is happening in front of them. The developers are going fast because
they are postponing tasks to the future.

The *invisible task backlog* is growing, but developers do not have the resources to deal with it, and product managers
do not see that pile. Most of product managers do not have no technical background, or they would rather simply ignore
the issues, and release.

The development pace start slowing down until any feature takes weeks or months instead of just days: *why are we so slow?*
Also the matter of quality arises: *why or project has so many bugs?*.

### Important: where the analogy fails

The tech debt metaphor was created as an analogy between the financial world and the software one. However, there is a missing
piece of the puzzle: the interest rate. When paying debt, there is usually an interest rate. However, the tech debt does not keep
the same interest as the time passes. If no technical debt reduction effort is done, the *interest rate* is also cumulative.
So instead of having a constant 1%, 2% increase of resources because of tech debt[^3], every year we find +0.5% or +1%
(or a similar value). The complexity keeps growing because we are keeping adding new features, modifications on the code base.

This increase is what people do not understand. If a library is deprecated and your project depends on it, you should immediately
start searching for a replacement. If not, it is only a matter of time when it becomes unsupported and bugs or CVEs start 
appearing. Add this to a tangled flow on the most important feature of the project that needs to be changed, an outdated runtime,
and no tests, and the project is a house of cards.

 This phenomenon is like *an escalator that not only goes down when we try to climb up, but it keeps accelerating its descent*. **The entropy always grow unless we dedicate an effort to keep it contained**.

## What can be done to reduce it?
The best way to tackle the tech debt is to keep it minimal from the start.
**Refactoring a code that is tech debt ridden should always be the last resort.**

### Rules/Guidelines/Culture
Advocating for creating a culture of responsibility and quality is a must.

Clear guidelines on:

- Development guidelines.
- Design patterns.
- System design.
- Testing on all flows.
- Coding quality rules.
- Code formatting.
- Code review process.
- Security audit processes.

All of them are the bare minimum to contain the chaos that can be born on a software project.

Unless you are creating software that can automatically be verified (like in some programming languages), every software
developer/engineer has a different background and different preferences. While we must respect that, we need to set clear
boundaries about what is accepted, and what is not.

### Automatic enforcement

However, I do not think this is enough for keeping the tech debt at bay. The temptation of going faster is going to always
be there, and the PMs are going to be always pushing.

This is my favorite way of keeping tech debt to a minimum: to have a series of pipeline jobs that analyze the code and
detect formatting issues, [bad smells](https://martinfowler.com/bliki/CodeSmell.html) on your code,
and any other issues that could be automatically detected.

Although I would rather use static analysis tools, now that we have LLMs, we could even describe the guidelines as context in the project and run the LLM on each one of the files that the developer has modified.

If we force to have different tests we also will be ensuring good quality. There is an adage that says:
*good code is easily testable code*, and I would say it is true, as the pain of having to deal with the bad code
is felt by the same developer that has created it. Add some rules to the tests, and now you are golden!

Keep in mind that testing is not replaced by static analysis, nor by LLM-based code analysis. A good codebase has tests always,
and while tests do not guarantee that the code has good quality, not having tests guarantee a bad codebase.

Indeed, I would rather have a lot of static analysis tools and testing than LLMs. LLMs can be unpredictable:
they hallucinate and depend on their training data. Maybe the data is outdated, or is outdated with bad practices.
Anyway, do not trust LLMs solutions blindly[^4].

Some tools that you should be using:

#### NodeJS

- [eslint](https://eslint.org/docs/latest/integrate/nodejs-api)

#### Python

- [black](https://black.readthedocs.io/en/stable/)
- [flake8](https://flake8.pycqa.org/en/latest/)
- [isort](https://pycqa.github.io/isort/)
- [pyflakes](https://github.com/PyCQA/pyflakes/) (I reckon that I have not used it)
- [mypy](https://mypy-lang.org/) or [ty](https://docs.astral.sh/ty/)
- [pylint](https://www.pylint.org/) or [ruff](https://docs.astral.sh/ruff/)

In case you want to see an example of these tools in action, see my
[format check GitHub action](https://github.com/diegojromerolopez/otelize/blob/main/.github/workflows/check_format.yml#L21)
in my open source [otelize](https://github.com/diegojromerolopez/otelize/) Python library.

#### Ruby

- [Rubocop](https://rubocop.org/)
- [Reek](https://github.com/troessner/reek)
- [flay](https://github.com/seattlerb/flay)
- [flog](https://github.com/seattlerb/flog)
- 

Flay and flog are very hard to work with, but they can give you a lot of pointers of code that needs to be refactored.
I remember reading the [Confessions of a Ruby Sadist website](https://ruby.sadi.st/Ruby_Sadist.html) almost 10 years ago.

I do not recommend using [heckle](https://ruby.sadi.st/Heckle.html) as it seems to be unsupported.

## Conclusion
Reducing tech debt once that is there is costly, and usually involves rewriting parts of the project. It is much better
to rely on tools that contain it. These tools need to be visible to the developers and to the product managers,
as the efforts to reduce technical debt must be considered as part of all development tasks, always. No exceptions.

Rewriting software should always be avoided.

[^1]: I wrote about this in my [MRes. thesis](https://github.com/diegojromerolopez/djbdd/blob/master/doc/memoria.pdf).
Sadly there is only a Spanish version, but you can take a look at the library
[djbdd](https://github.com/diegojromerolopez/djbdd) that I created for that.

[^2]: Usually those are codebases that had no abstraction, no structure, everything is at the same level.
They do not enforce guidelines, nor in the format nor in the design. The *tangled* part comes from having
dependencies all spread through the code.

[^3]: I have not taken into the account the inflation. If the inflation is greater than the interest rate, it can be
a good financial decision to delay payments. For the sake of the argument I have left this concept out. This
post is not financial advice.

[^4]: Yesterday I asked a LLM to create a test that depended on the current time and it set a constant time as input.
That test was working perfectly, but it would have failed in a couple of weeks.