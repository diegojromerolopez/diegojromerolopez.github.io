---
title: Software quality is not negotiable
date: "2025-03-15T00:00:00+02:00"
draft: false
tags: ["software", "quality"]
---

# Software quality is not negotiable
From a conversation from one of the best software engineers I have had the please to work with,
I heard the following sentence: *software quality is not negotiable!* And that is one of the
axioms of our profession.

## Why software quality is seen as optional?

## Software developers/engineers come from different backgrounds
The world of software has no barrier entry. People with different backgrounds can start working
as software developers or engineers. That is a good thing as diversity can enrich the organization
but there is also the matter of different perceived levels of professionalism in the discipline.

In my experience, most of the developers that do not come from an engineering background have a
lesser view of quality.

## Software practitioners are pressured to disregard quality
The product managers, team managers or even executives can push software developers to not take
all the necessary steps with respect to quality. It can be as simple as overworking them or
just pushing some artificially defined deadlines on them.

I have experienced these two scenarios, and you need to know if it is worth it to pursue a confrontation
against the managers for this. If they do not see the value in ensuring quality, maybe you wonder if that
team is the best place for you.

## The rules of the market are ferocious
New software companies a.k.a. *startups* tend to be forced to avoid adding tests and just relying on
automatic (or even manual) QA testing. I *kind of* understand that in this environment, being
worried about quality is a second thought. Having to pivot and deliver features to the market and react
to the feedback is the way to go.

However, the code should be implemented in a way that eases the creation of tests, because creating tests
for a code that needs to be refactored is not always an easy task.

## *Outsiders* do not have clear picture of the quality
Some time ago a marketing person said
*why do you need to touch that [meaning a piece of software] if it works fine?*.

Most *outsiders* do not understand the peculiarities of software development. Concepts
like dependencies, deprecation, version removal, support or tech debt are totally foreign
to them.

Software is a living thing. It is not static and needs to be maintained all the time. Unless
your software is proven to be correct and has no dependencies, you would need to spend time
on the project to ensure that its dependencies are up-to-date, and the requirements that justify
its existence are met.

## Tests have a bad reputation
This is my favorite, most software developers do not know how to write tests, nor the different
types of tests that are, nor how to write good tests.

Most unit tests tend to mock everything and just ignore the purpose of unit tests:
enforce contracts among the different layers of the software.

Integration tests are not done most of the time. Or they are confused and put
together or alongside the unit tests.

End to end tests are not done or if they are, only the *happy paths* are tested.

## Conclusion
Software quality is not negotiable, as quality in most parts of our lives is not.
