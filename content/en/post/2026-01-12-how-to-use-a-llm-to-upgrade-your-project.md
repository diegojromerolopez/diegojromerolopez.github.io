---
title: How to use a LLM to upgrade your project
date: "2026-01-12T00:00:00+02:00"
draft: false
tags: ["llm", "ai", "guide", "showcase"]
---

# How to use a LLM to upgrade your project
In this post we pick up a Python 2.0 project and show how to use a LLM to upgrade a software project.

## Introduction
I will upgrade the [Djanban](https://github.com/diegojromerolopez/djanban) project
as it should be done. Not only making it work with the latest versions of the software
packages, but improving its quality and making sure there are guardrails that make impossible
for the developers 

## The problem
As explained in the [previous post](/blog/2026/01/how-not-to-use-a-llm-to-upgrade-your-project/),
the backend of Djanban was implemented in
[Python 2.0](https://www.python.org/doc/sunset-python-2/) and Django 1.11.
Python 2 has been outdated  for 6 years now and is not used anymore. Django is now in version
[6.0.1](https://docs.djangoproject.com/en/6.0/releases/6.0.1/).

The frontend of Djanban was implemented in Angular and I have not touched Angular in almost a decade, as it was surpassed by React as the go-to frontend framework a long time ago.

I want to do an upgrade but that improves the quality of the project too.

**I want to upgrade and improve the project**

## The tool
As I did earlier, I am using [Antigravity](https://antigravity.google/) with the model
[Gemini 3 Flash](https://deepmind.google/models/gemini/flash/, because I reached my limits of the model
Gemini 3 Pro while running doing the upgrade for the [other post](blog/2026/01/11/how-not-to-use-a-llm-to-upgrade-your-project).

Anyway, I am not trying to have perfect comparison scenarios, but a *coarse-grain* ones.

## The challenge
Upgrade everything to the latest version and make it work, but improving the project.
This project was created as a proof of concept, and seriously lacks the quality expected
for a Software Engineering project. This needs to change.

I will be using *vibe-coding* as in our previous run with the zero-shot prompts.

## The process

### Use the old versions
When dealing with an outdated project, the first step is to replicate the environment to run it with the exact same
runtime and packages. In my case, we are talking about a Python 2.7 project, so as I am using asdf, I installed
the last version of Python 2 in my laptop:

```sh
asdf install python 2.7.18
```

and set it to be the Python version in the folder.

```sh
asdf set python 2.7.18
```

### Ensure the current functionality

I wanted to preserve the functionality so I asked Gemini to create tests for every file.

This is the prompt I used:

```
Create a virtualenv for Python 2.7.18, activate it, and install all the packages there with pip. Use always the activated Python 2.7.18 interpreter it to do any action in this project unless I told you otherwise. After that, create unit and integration tests (with unittest) for each djanban file and ensure the test coverage is 100%. The tests must be in src/djanban/tests/unit and src/djanban/tests/integration. Every test file must be placed in the analogous relative path than the tested code but with a root path of src/djanban/tests/unit or src/djanban/tests/integration.
```

As you see, I also made it clear that they need to use a virtualenv with the outdated Python version.

```
Please run the tests and show the covered test lines
```

To ensure that the files were actually covered.

[See the commit](https://github.com/diegojromerolopez/djanban/commit/d723f9a08f1abe66de71593a727deaddd5fbd3ca) with the changes.

### Upgrade Python version

```
Upgrade Python to 3.13.5 and migrate al the source code to the new Python version. Leverage the tests to ensure the functionality stays the same.
```

The same mistake that in our previous post happened! The versions are not fixed, is this because the LLMs have learned a bad
practice from thousands of repositories on GitHub?

[See the commit](https://github.com/diegojromerolopez/djanban/commit/b2cd6782d6937381fe2dfe9b17dd48c3a4c15f2d)
with the migration to Python 3.

```
Ensure the migrations work and freeze the requirements to minor versions. Create dockerized version of the application.
```

[See the commit](https://github.com/diegojromerolopez/djanban/commit/af164eafb7cd21cc47292f0b52803ef25f65e6a5)
with the last changes.

### Upgrade Django version

```
Upgrade Django to the last version (6)
```

This is on me, Django was already set to 6 in the requirements.txt.

```
Django~=6.0.0
```

To be fair, now there are like 3 requirement files, so let's clean that up:

```
Clean up the requirement files. THere are 3 of them and at least the main dependencies should have the same versions.
```

I did not even tell the AI Agent that there are several requirement file depending on if we want the development dependencies
or else. But it did a good job ([see the changes here](https://github.com/diegojromerolopez/djanban/commit/8bfbe0edde9c42df0283d6f226acf3de02124640)) it re-used the main requirements.txt file in the other files, avoid repetition.
A good practice indeed!

### Enforce format

Now, having the code format of the community is paramount. So I am going to re-format the source code to comply with the
de-facto community rules. We will use the following tools:

- [black](https://black.readthedocs.io/en/stable/)
- [flake8](https://flake8.pycqa.org/en/latest/)
- [isort](https://pycqa.github.io/isort/),
- [pylint](https://www.pylint.org/)
- [ruff](https://docs.astral.sh/ruff/).

I would have liked to add [mypy](https://mypy-lang.org/) for type hint checking, but the code has no type hints.
I programmed this application in Python 2, so no type hints at that point.

These tools provide a good baseline to have a standardized source code in Python projects. Sure I could remove pylint,
as ruff more or less have the same features, but I keep using pylint because
[pylint has plugins](https://pylint.readthedocs.io/en/latest/development_guide/how_tos/plugins.html) while ruff has not.
So, in the case of finding a good pylint plugin that can enforce a better source code quality, it is just a matter of
installing the package and enabling it.

Anyway, this is the prompt I am using:

```
Clean up the project. I want all the code to be formatted by black, flake8, isort, pylint, and ruff. Add the corresponding badges to the README.md.
```

As expected, leveraging on source code analysis tools works pretty well in conjunction with an AI Agent
([see the changes here](https://github.com/diegojromerolopez/djanban/commit/a63698daad6cf51fa53fd8bc067b83e69329e8e5)).

### Building a pipeline based on GitHub actions

I like to *set the functionality in stone* by enforcing testing and the format in the pipeline:

```
Now add github actions that run each time the pipeline runs. These actions must run the unit tests on one job, the integration tests in other, and a format check in another job.
```

The AI Agent failed here as nor the
[format](https://github.com/diegojromerolopez/djanban/actions/runs/20902794227/job/60051298977),
nor the [unit tests](https://github.com/diegojromerolopez/djanban/actions/runs/20902794227/job/60051298972)
nor [integration tests](https://github.com/diegojromerolopez/djanban/actions/runs/20902794227/job/60051298970) passed.

A thing that I did not like at all, is that the AI Agent understood that I wanted them to run git commands, and
they did. They created two commits for this prompt:

[See the first commit](https://github.com/diegojromerolopez/djanban/commit/6ea9a6b3905252f0bded4bec4d91a8240866015a),
and the [second one](https://github.com/diegojromerolopez/djanban/commit/8db1247423565c6e486d7284deb3a204c7bdb7a5).

### Upgrading the Angular app

Let's forget about the GitHub issues, and let's try to upgrade the frontend that is based on Angular App.

```
Create tests for the Angular App and once you have them in place, upgrade it to the latest version.
```

To be fair, I do not remember anything about Angular, so I cannot give the agent any directions whatsoever.
We will need to use this *shot-in-the-dark* approach for the frontend.

After a while, I consumed all my weekly quota and was forced to choose other model.
At this point, I was not interested in reproducibility nor in comparing different models but in
the **experience of upgrading with *vibe-coding***, so I chose
[Claude Sonnet 4.5](https://www.anthropic.com/news/claude-sonnet-4-5) and run the following prompt:

```
Ensure the tests for the Angular App are in place and that the application is upgraded to to the latest version.
```

Not even the LLM could give me a full solution, it warned me that it has created a new application that had a lot of issues:

```
Recommendation
Given the complexity and the fact that the legacy app is extremely outdated and insecure, I recommend we:

Document the current state - The new Angular app structure is in place with core services migrated
Add the new app to git - Preserve the migration work done
Create a migration plan - The remaining components need careful migration due to their complexity
```

So I resolved to stop here. I am running blind and the LLM is doing that too (on one hand they are telling me the migration
is done, but on the other, the agent is telling me the opposite).
**It seems that while most outdated dependencies and most outdated the framework/library/application is, the harder it gets**.

9 years ago I added the node_modules folder to git. Big mistake! So now I needed to ignore it:

```
Ignore all the node_modules in git
```

In case you want to see
[the commit](https://github.com/diegojromerolopez/djanban/commit/5b86f76c3d302a56933cf2785815699dcd7d828b),
this is the sub-par work the LLM has done.


## The results

## The bad

I did not like is that at this point, the Antigravity editor was showing modified files that were already
saved and pushed to the repository. For some reason it was unable to detect that they were not actually modified.

I was not able to run the same model than in the other experiment because I reached my limit just by playing around.
I get that they want us to pay more, but... I was disappointed but the low limits for a paying customer.

## The good

A project that was outdated and abandoned can be brought to life by leveraging the AI technologies.
What a wonderful thing!

As long as you give orders to the AI Agent they will do it. The issue is that you need to know what to tell them
to make their actions meaningful and correct. **You need to be exhaustive in your orders**. Do not assume the agent
has enough context to understand you correctly.

Leveraging tests to make changes without introducing bugs takes a new form in the LLM-assisted software development.
If before that we needed to have a cycle of red-green testing and refactoring. Now it is much faster, but the concept
is the same.

I had to trust the changes in the Angular app as I do not remember most of the framework. It is not a critical part of the
application itself, Angular was only used in the Kanban board, but it gives me a bitter taste in the mouth to have to
trust a LLM completely. Of course I could run the app, but that defeats the purpose of this experiment.

## The ugly

I should have ben more careful when asking the AI Agent to create the GitHub actions, to avoid an accidental
commit in the repository. It is not a big thing, but I like a clean git history. A history that I can traceback
because I have done it.

I need to fix the GitHub actions by hand. I need to investigate if you can give permissions to the agent to do actions
in only one project. If that is the case, I will use the LLM to fix the issues.

The Google AI Plans have a very aggressive quota for personal developers. I am not sure it is worth it to have it.

# Conclusion

Just by **knowing what to ask** to the AI Agent in the conversation we obtain much better results than just doing a
blind prompt with a vague requirements. Running LLMs and creating software applications does not mean you are a
software engineer. Using LLMs to create maintainable, extensible, and performant software means you are a software engineer.

Along the decades of our profession there has been a lot of technological advances, and this is the most surprising of all of them.
However, this technological marvel does not remove the engineer from the loop.
It frees them from some *menial* or repetitive tasks.

This has been a good experiment showing that the human factor that *steers the ship* is still needed.
We do not know what has the LLM learned, so they could be generating bad patterns or designs.
