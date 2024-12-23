---
title: CV Driven Development
date: "2024-12-23T00:00:00+02:00"
draft: false
tags: ["leadership", "war-story", "corporate", "training"]
---

# CV Driven Development
[CV Driven Development](https://www.clairecodes.com/blog/2019-05-15-cv-driven-development/) or
Resume Driven Development consist on taken strategic decisions based on how they improve
the CV of the developers that work on that project.

## Introduction
Most of the project management methodologies have a focus on improving the satisfaction of the
clients and users. Most of the time by removing friction between them and the development process,
or by reducing waste.

CV Driven Development has as one of the non-functional requirements *learning something new*. It does
not have to be a bad thing, but if it is not done properly, it can be chaos when dealing with
maintenance of the project.

## But why do they do CV Driven Development?

### Training time is working time
Software development is a demanding career that pushes developers to work a lot in their free time.
Some of them decide that that is not enough or that they do not want to spend their free time learning
the last shiny framework, so they push for the use of new technologies, patterns, architectures on
their day to day job.

Most of the professions do not expect you to learn on your free time (although some do). And all intellectual
professions give resources to workers to learn on the job.

> *Train people well enough so they can leave, treat them well enough so they don't want to.*
> Richard Branson [source](https://www.linkedin.com/posts/rbranson_train-people-well-enough-so-they-can-leave-activity-7094663480783327232-WDuo/)

### Greenfield project
What a better way to improve your CV than working on new technologies in your day job. If the company
provides a *greenfield* environment for developers to work on new projects, it is expected that there
should be a *spike* to research the different technologies and designs that will better fit the
requirements.

## Software Engineering is subjective
Software Engineering is subjective. The programming language you like is not liked by your team mate,
those pesky singletons are loved by other teams, and you may love typed languages while all your
company developers despise them. Don't get me started with the project management methodologies.

Now, I want you to think about this question: *Does make it sense to use a tool just because you like it?*

## Software Engineering is based on heuristics
We have seen that the Software Engineering world is vast and diverse, there are a lot of points of view
(some of them are opposites, in fact). I prefer to base my technical decisions with experiences and not
in personal preferences.

## War stories

### What to do
I worked for a company that had strict rules about technologies, framework and libraries: only some
languages were approved in some context (backend, frontend and such), each team determined the
framework to use (sometimes it was developed in-house) and the libraries needed to be approved one by
one by the team. No fancy libraries that were proof of concepts or that had few users were accepted.
Even when they seem to be useful.

Navigating the projects were easy as all of them were *boring* and everything worked as expected.
Was the top-of-the-notch company? No, but there was never an outage in production during my time there.

I usually depict my time there as one of the pushers of a gigantic wooden chariot. The chariot (let's
call it a *Juggernaut*) is being pushed by a myriad of engineers and developers. If there is some issue
in a side (like a hole in the ground) more people can push on a side to overcome the obstacle. Now, the
chariot goes very slow, smashing all the things it finds on the ground. Nothing can stop it. It is
indestructible.

I know it is a *silly* metaphor about my time there, but it is useful to explain my feelings of the
safe and sound work that took place there.

### What NOT to do
I worked for other company that granted a lot of liberty to the developers. It was an heterogeneous
ecosystem with projects developed in several languages, with different architectures, etc.

One developer decided to apply CV Driven Development and pushed for using a complex architectural pattern
on a simple API server project. To make matters worse, the language to implement the project was a niche
one, mostly used in the context of mobile Apps.

There was only a guy that know the architecture and the language, he did not spend time training other
developers and when asked about the inner workings he just gave a short unuseful answer.

As you can imagine, extending this project was *madness*. The project was faulty to say the least, and
working on it was painful.

We ended up replacing the project entirely because the onboarding there was a pain in the back.

## Conclusion
While learning on the job is fine and should be encouraged by the managers and executives, however
all the team members should *be in the same page*, i.e. all developers of the team should learn
at the same pace, and if that is not possible, mob programming or review sessions should be done
to ensure all developers have a basic idea of the *new thing*, i.e. **always spend time training the team**.