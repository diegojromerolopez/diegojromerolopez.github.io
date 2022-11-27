---
title: Actual integration tests
date: "2022-11-27T18:47:00+01:00"
draft: false
tags: ["testing", "software engineering"]
---

Many times we have some piece of code that is tested but is still failing
in production. How is that possible? Is that because of bad tests or
we have a greater hidden issue?

# Protect your vital functionality with integration tests

Integration tests are the best way make sure that a functionality
does not degradate when adding new features.

## What are integration tests

Integration tests are tests that check a full feature of the project.
So, in the case of adding new features, we can guarantee that at least
the covered features are going to keep working as expected.

## Unit test vs Integration tests

**Unit tests** check only a part of the project and usually rely in *stubbing*
and *mocking* many dependencies, i.e. they do not test everything, as many
parts of the checked code are replaced by *fake* functionality.

**Integration tests** does not rely in faking all the dependencies of the project
(or that is the goal, sometimes it is not possible and some mocks needs to be used).
They fully check a feature end-to-end.

Both cases are needed to allow easy refactors of code and detect integration
errors before reaching production. However, integration tests provide a
better way of assuring the project's feature, as unit tests can fail
to rely too much in mocking some module's dependencies. Most of the times,
integration tests only mock external services, hence testing the actual
functionaly of the project (unlike unit tests).

## Smoke tests

There is a kind of tests that have the aim of making sure the basic
functionality of the project keeps working after having added new features.

Examples of these tests are "signing up an user", "logging in an user",
"selling a product to an user", etc.

These tests give "mind peace" to developers, as they guarantee some basic
features. Usually there are no smoke tests for all the features that the
project has, but for the most commonly used. That way, in the event of
a *bug*, there would be a *degradation of the service* but never an
error as it would have been detected in the testing phase.

## How to do it?

Try to replicate the production environment as good as possible when
creating the integration tests.

For example, thanks to docker container technology,
it is possible to run [docker containers inside
docker](https://hub.docker.com/_/docker), and hence create
a mini-production environment to test.

Another way to do it, is to have a clone of production and deploy there
each time the contionus integration runs, and run some test again that
production clone server.

There are multiple ways to do it, but you have to found a way to have
a test environment as similar as possible to production with the possibility
of running tests there.

# Conclusion

Create meaningful integration tests for your projects. Smoke-tests
are a good way to make sure the basic features of your project
keep working after including a new feature.
