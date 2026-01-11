---
title: How NOT to use a LLM to upgrade your project
date: "2026-01-11T00:00:00+02:00"
draft: false
tags: ["llm", "ai", "guide", "showcase"]
---

# How NOT to use a LLM to upgrade your project
In this post we pick up a Python 2 project and show how **NOT** to use a LLM to upgrade an
outdated software project.

This is a two-series go to the [next post](/blog/2026/01/how-to-use-a-llm-to-upgrade-your-project/)
if you are only interested in how to do it correctly.

## Introduction
I created the [Djanban](https://github.com/diegojromerolopez/djanban) project 9 years ago.
At that time I was studying a [Master's degree in Software Project Management](https://www.fi.upm.es/web/masterdgps/) by the
[Technical University of Madrid](https://www.upm.es/internacional).

## The project
Djanban was born as an extension of Trello. At that time, I implemented Kanban in a small team while I was working at 
intelligenia. So the aim of this tool was twofold:

- Provide a way of extracting advanced metrics and insights from the evolution of the tasks (bottle necks, ).
- Have an excellent control about the time spent in each task.

There was also a frontend that could be run to have total control of the state of each task, and even move the tasks.

Sadly I did not implement webhooks in Djanban, so I needed to probe Trello from time to time.
Rustic and inefficient, but it worked. Anyway, the final objective was to use Trello only as an interface
and Djanban as an insight-extraction engine.

## The problem
The backend of Djanban was implemented in [Python 2](https://www.python.org/doc/sunset-python-2/) and Django 1.11. Python 2 has been outdated  for 6 years now and is not used anymore. Django is now in version
[6.0.1](https://docs.djangoproject.com/en/6.0/releases/6.0.1/).

The frontend of Djanban was implemented in Angular and I have not touched Angular in almost a decade, as it was surpassed by React as the go-to frontend framework a long time ago.

The issue is that I would like to upgrade the code to supported versions, but I do not want to do it manually.
The project has a lot of files and I do not want to waste time upgrading them version by version.

**Could we use a LLM to upgrade all files simultaneously?**

## The tool
Let's use the simplest tool possible: [Antigravity](https://antigravity.google/) with the model
[Gemini Pro 3](https://gemini.google.com/) with [a developer plan](https://antigravity.google/pricing).

### Settings
After being authenticated in Antigravity with our Google Account (that has the Developer Plan),
the first step is to make sure all the edits are going to be done automatically without my intervention.
To do that, first go to the *Quick Settings Panel* on the top right corner:

![Antigravity account settings](/img/2026/01/11/antigravity-account-settings.png)

and click on the *Quick Settings Panel*.

Now on the emerged dialog, make sure you have *Always Proceed* in the Auto execution selector.:

![Antigravity quick settings panel](/img/2026/01/11/antigravity-quick-settings-panel.png)

To not worry much about the conversation with the AI Agent, I am going to assume they are right almost all the
time, and let them work and fix their own mistakes.

![Antigravity conversation settings](/img/2026/01/11/antigravity-conversation-settings.png)

## The challenge
Upgrade everything to the latest version and make it work, using the simplest prompts possible. No specs,
no context, no additional directions on my side (I am going to *ignore* their thought process). 
I want an empty AI Agent that discover by themselves the issues and fixes them.

I call this approach *Hands-off AI Agent assisted development*.

## The process

### First prompt

```
Upgrade all the code in this repository to the latest version both backend code (Python 2 and Django 1.11), and frontend code 
(old Angular code).
```

Here Gemini told me that the backend was ready for running it with Python 3.0 and Django 5.0 (not true), and 
they were not able to refactor the Angular App to make it work. Has changed Angular so much in
9 years? Would it be easier to just refactor the app to React as some people have done?

[Commit with the changes](https://github.com/diegojromerolopez/djanban/commit/c5718c90f94b821ff29e137418740804cb00208b)

### Second prompt

I asked Gemini to run the app to check if it worked:

```
run both the backend and frontend for me
```

After some minutes, I had a successful response from the agent telling me to go to http://localhost:8001 and
check the application running.

![Djanban running](/img/2026/01/11/djanban-running.png)

It has been a while since I have seen this bootstrap-based interface.

[Commit with the changes](https://github.com/diegojromerolopez/djanban/commit/8e1165f5feb54859e8ae1e40c34cbca62b78aeae)

### Third prompt

But I do not remember the user nor the password, did I create one by default in the application or how did it worked?
So I asked the agent to create one for me.

```
What's the user and password? Could you create one for me?
```

And the agent created a new account admin/admin for me by leveraging the Django manage.py shell.

![Djanban logged user](/img/2026/01/11/djanban-logged.png)

## The results

You can see the upgrade in the branch [feat/upgrade](https://github.com/diegojromerolopez/djanban/tree/feat/upgrade)
on the Djanban repository.

### The good

**The application works**. There are a lot of horror stories about migrations from Python 2 to 3. The release process
was not the best and the community ended up fractured and disappointed with the project leaders. The migration process
lasted more than a decade and a lot of conflicts both in software and at human level. Having an AI Agent that can
reduce the pain of doing such an upgrade that is costly in time and in resources.

### The bad

The AI Agent did not clean up the code. They left all the files with the UTF-8 header comment, even though it is not
necessary anymore because Python 3 files are UTF-8 by default.

Extreme laziness on their part. Not only the AI Agent did not clean up the code, removing unnecessary comments, but
it ignored important parts of the project because they could not migrate it. I am talking about commenting the indexes
of all models because the format was changed in Django 5.1. The AI Agent even created a script for this: [src/comment_index_together.py](https://github.com/diegojromerolopez/djanban/blob/c5718c90f94b821ff29e137418740804cb00208b/src/comment_index_together.py)).
Anyway, this is serious, as having no indexes can affect greatly to the performance of the application.

The AI Agent did not create a virtualenv. So they ended up installing all the packages in my system Python installation.
In almost no place it is recommended this approach as it pollutes the system Python libraries. 
**The agent should have created a virtualenv**, and install the packages there.

In the 
[requirements.txt](https://github.com/diegojromerolopez/djanban/blob/feat/upgrade/src/requirements.txt) 
the package versions were left open. The only restriction it in place was that Django needs to have at least the version 5.0, 
while the [5.2 is a LTS version supported as of the 10th of January of 2016](https://www.djangoproject.com/download/).
You should not do this ever. In the case of a package, I can understand leaving the dependencies boundless, but for an
application it can be catastrophic. An upgrade can cause an instant outage.
**If your dependencies follow the semver release cycle, fix the major versions to avoid breaking changes**.
If you have dependencies that do not specify their version policies,
**just set a fix version for these untrusted (version-wise) dependencies**

What does it mean that the agent cannot upgrade Angular? Not even create a basic interface?
Did Angular change so much in the last 9 years? I would not know as I have not touched that framework since then.
Maybe [I should have directed the agent to be more *adventurous*](https://www.taskade.com/convert/coding/angular-to-react).

### The ugly

As you can guess, my scenario is biased. I was not involved in the process as I should have:

- I gave very limited prompts to the AI Agent.
- I did not provide any direction on what good practices should use.
- It is not that I gave a bad context: I gave no context at all. No role-playing, no additional information.
- Use any code conventions. Although it is not critical, having a linter and fixing the issues the linter found can improve
the quality of the code a lot.
- There are no tests so there is no way to automatically test that the changes are correct. I could have created tests first,
but that would have been cheating.

I will do the same experiment but in a more structured way to compare the two results.

# Conclusion

You cannot leave an AI Agent running unsupervised when working on upgrades. It is true that the agent can do the required
upgrades, but it will make mistakes, and you need to be giving directions.
