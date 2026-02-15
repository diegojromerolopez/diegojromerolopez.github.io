---
title: Cloud-Only Testing: Convenience vs Risk
date: "2026-02-20T00:00:00+02:00"
draft: true
tags: ["testing"]
---

# Cloud-Only Testing: Convenience vs Risk
The cloud did not removed complexity, it only centralized it.

The infrastructure became more programmable, flexible, scalable, and abstracted.
But that did not mean that the systems became simpler.

## Architecting for the cloud

The cloud companies were born as a way to reduce complexity for the engineering teams.
However, the complexity was not removed, but moved from the engineering teams to the cloud systems.

But creating complex architectures in the cloud has a clear counterpart: how can we ensure they work properly?
How can we make sure that our solution does the right thing, and is sufficiently performant?

Testing the project in a *live* environment is the natural choice for assessing the correctness, scalability, and performance.

## Cloud testing strategies

When people show the testing pyramid they make clear the distinction among the different types of tests,
but they just group all the end-to-end tests together. In my sixteen years working I have worked with
teams that had several strategies that take in consideration the service mesh that is our full project.

On these strategies, testing is done end-to-end, in the case of web services (the usual one), by running
headless-browser or batch http request scripts against the environment running on the cloud.

These tests can be run in the pipeline, and use one of these environments as a black box that needs to be checked,
or it can be tested with a more traditional QA approach: running an assessment on the service. This can be
manual or automatized.

### System tests

#### What's it?

A job in the CI/CD pipelines that run a series of tests that depend on cloud services. A sort of end-to-end test
that are part of the project tests.

#### Pros

It is easy to implement, as the tests are part of the project test harness.

There is no need for mocking services, as the tests use the actual real cloud services.

#### Cons

Require a live environment but it cannot be used for manual testing, as it will be modified again and again when the CI/CD pipelines run.
If it is the same environment for all runs, there can be conflicts.

Connecting a pipeline job to an environment can be a challenge from the security point of view.

### Playground environments

#### What's it?

Allow deploying any *change* on a project on an isolated environment. If you need to test a feature,
deploy to this *partial mirror* of production, but that only contains the services you want to test.

Deploying to this environment is not a requirement and checking the changes in this environment is seen
as a good but not mandatory practice. However, as it is difficult to replicate the production services in this
playground environment, most of the times I have seen this strategy, there was limited testing here, and the
dependencies were usually supplanted by mock services.

This strategy is done by allowing deploying developers in their feature branches, and allowing them
to deploy their dependencies by using the same branch name.

#### Pros

You achieve total isolation for testing. Developers can run destructive operations on the environments
without any care at all. No other developer nor user is going to be affected by that.

Total customization of the state, data, and code is possible.

If the ephemeral environments are mirrors or similar to the production environment, the development pace
can be much faster as the tests and QA assessment can be done in parallel.

#### Cons

The cost can *skyrocket*. We are talking of replicating the production
environment every time a developer wants to test their changes. If they
are not careful, we can find ourselves with a big cloud bill.

We need some balance between production-similarity and cost. Having an
environment more production-like will be expensive (as all of its services
need to be deployed). On the contrary, just having a bunch of mock servers
talking among each other can be cheap, but useless.

Management of the state of the environment can be painful. Starting up, restarting them,
and above all shutting them down are operations that need to be done frequently.
So they need to be implemented in the ecosystem as first-citizens.

Given the ephemeral nature of these environments, there needs to be an import of data,
that needs to be curated to work with the mock services. That work cannot
be disdained.

### Pre-production environment

#### What's it?

A full mirror of the production systems, with all the dependencies. Changes here are a mandatory step before
deploying to production. Once you have reached this environment, it is assumed that the code has enough
quality for production, and has been tested by the software engineers (and maybe by the QA engineers).

There is only one pre-production (sometimes called staging), as the environment is linked to the default branch.
Production and staging are only in the same branch and different commit (production is always behind or at the
same level than staging).

#### Pros

It is much cheaper to keep a lone mirror of the production environment, than potentially *infinite* ones.

Given that the data stays in the environment, it is more difficult to start the tests from a clean slate.

Also, the environment is up all the time. There is no need for implementing operations that grant the shutting down,
starting up, or restart operations to the developers[^2]. In case of issues the devops team can do these tasks,
because they are only happening on an environment, so there is no need to grant special privileges to the developers.

#### Cons

Conflicts, serialization, and deployment dependencies appear as soon as we use this strategy. The environment
becomes a shared resource, and it causes friction among teams as once a new deployment is complete, it will
replace the state and data that was there in the pre-production environment.

Do not disregard conflicts for a shared resource, as if the project is used by many teams, and each team has
5-7 developers, we can find ourselves spending a lot of time dealing with the synchronization of the
deployments on the pre-production environment. This downtime not only is a waste of time, but they can be
demoralizing for the developers.

### Production environment

#### What's it?

By deploying in production we can just test the feature in production. This is done by setting the new feature
under a feature flag, so the old behavior is preserved unless we decide to do the updated way.

Sometimes it is difficult to implement this change with feature flags, because maybe the change is
destructive and affects several parts of the service, rendering several of them unable to work as they were.

The test is done by setting a flag and running the operation via a headless browser.

#### Pros

There is a much lower cost of maintaining the environments in the cloud. There is only one.

#### Cons

A bug can be promoted to production, so the design of the feature flags needs to be done very
carefully to not crash the production environment.

The hardest part is not toggling the feature flag, but making the software so resilient that in case
of an update of the data in any of the data stores, the application does not crash.

What happens if the feature needs to be tested and has overlap with another one already deployed?
It will need to wait. So we have a similar situation of having a shared resource for the developers.
Not as dramatic as with the pre-production environment, as the changes are under feature flags,
but there can be conflicts among the developers.

Dealing with feature flags is risky. A bad configuration can enable features that were not supposed
to be public yet. Even worse, *buggy* features can be enabled by mistake.

To sum up, we trade devops complexity by software complexity.

## Limitations of testing on the cloud

Apart from the specific issues that have been named, there are several problems
with running the tests on a cloud environment: consolidation of architectural
mistakes and cost.

### Consolidation of architectural mistakes

First let me explain that when I say *test the design*,
I do not only mean testing that the design is correct, but that it performs well,
and scales well. Just *throwing money* to a problem in the cloud can solve any issue you find, it is tempting
but that is not the optimal solution.

The temptation of just accepting the first iteration of the architecture can anchor the project in a
sub-optimal and static architecture that can be painful to improve.

As you cannot really test the architecture before having all deployed in your cloud provider,
a mistake in the design becomes permanent.

### Cost

At the end of the day, running in the cloud is going to be more expensive than running in your local.
You are paying processing capacity, memory, data storage, and transfer. Maybe it is not much for a test,
but if your architecture comprises hundreds of services, and you need to keep an environment just for
testing, you are effectively doubling your cloud bill.

In other words: **your infrastructure works fine, but at what cost?**

## Conclusion

None of these testing strategies remove complexity.
Every strategy moves the complexity to a different place: organization, infrastructure, or software.

- **System tests**: implementation of end-to-end tests with real infrastructure in your pipeline.
Keeping in mind that the target environment is owned by the pipeline.
The early iterations of end-to-end-tests tend to be coupled with the architecture.
- **Playground environments**: most expensive. Useful for achieving total isolated tests,
and the dependencies can be mocked easily. Infrastructure complexity will be the one that needs to be tackled by the devops team.
What you gain in flexibility you pay in day-to-day operations.
- **Pre-production environments**: expensive, as it replicates the production environment.
Use it when there is no way to transfer the changes to production, and it is not going
to be conflicts among the developers for the use of the environment.
Complexity will be organizational mainly as there is a shared resource.
Synchronization among developers will be the main issue to solve in this scenario.
- **Production environment**: cheapest but most dangerous. Use it only when the cost of
replicating the environment is prohibitive. Complexity stays in the software realm.
However, it will increase: backwards compatibility, migrations, and feature isolation
will need to be dealt more carefully by software engineers.

Testing is a risk allocating decision, not a resource, nor skill decision.

Complexity does not disappear when using the cloud, it only centralizes it.

[^1]: master or main, meaning your default branch.

[^2]: do not disregard the maintenance cost of having to shutdown, restart, or start environments for each developer.
