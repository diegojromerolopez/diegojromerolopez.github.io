---
title: Reducing Risk When Developing Against AWS
date: "2026-02-20T00:00:00+02:00"
draft: true
tags: ["testing"]
---

# Reducing Risk When Developing Against AWS
A lot of companies use the cloud, specifically AWS, but few of them have a strategy to
ensure they can simulate and test their product before putting it in the cloud.
That is assuming a lot of risk. Is there any way to reduce the risk of a failure
on the software architecture?

## Introduction

## Architecting for the cloud

The cloud companies were born as a way to reduce complexity for the engineering teams.
However, the complexity was not removed, but moved from the engineering teams to the cloud systems.

Now Amazon Web Services (AWS) is the unparalleled king of the cloud platforms. It was one of the first companies
to offer services like S3, ECS, and such. Using AWS removes operational cost but hides system complexity
behind APIs.

But creating complex architectures in the cloud has a clear counterpart: how we can ensure they work fine?
How we can make sure that our solution does the right thing, and is sufficiently performant?

If we were talking about a software, I would propose testing the software, but now that we have a mesh of
different services that depend one with another we need to test the full project, including the communication
among the different services.

## Testing strategies

When people show the testing pyramid they make clear the distinction among the different type of tests,
but they just group all the end-to-end tests together. In my sixteen years working I have worked with
teams that had several strategies that take in consideration the service mesh that is our full project.

## Testing on the cloud

On these strategies, testing is done end-to-end, in the case of web services (the usual one), by running
headless-browser or batch http request scripts against the environment running on the cloud.

This tests can be run in the pipeline, and use one of these environments as a black box that needs to be checked,
or it can be tested with a more traditional QA approach: running an assessment on the service. This can be
manual or automatized.

#### Playground environments

Allow deploying any *change* on a project on a isolated environment. If you need to test a feature,
deploy to this *partial mirror* of production, but that only contains the services you want to test.

Deploying to this environment is not a requirement and checking the changes in this environment is seen
as a good but not mandatory practice. However, as it is difficult to replicate the production services in this
playground environment, most of the times I have seen this strategy, there was limited testing here, and the
dependencies were usually supplanted by mock services.

This strategy is done by allowing deploying developers in their feature branches, and allowing them
to deploy their dependencies by using the same branch name.

Given the ephemeral nature of this environments, there needs to be an import of data, that needs to be
curated to work with the mock services.

#### Pre-production environment

A full mirror of the production systems, with all the dependencies. Changes here are a mandatory step before
deploying to production. Once you have reached to this environment, it is assumed that the code has enough
quality for production, and has been tested by the software engineers (and maybe by the QA engineers).

There is only one pre-production (sometimes called staging), as the cost of maintaining
and running the production environment can be prohibitive.

That is why this environment is linked to the master[^1] branch, in the sense that production and staging are only
in the same branch and different commit (production is always behind or at the same level than staging).

Given that the data stays in the environment, it is more difficult to start the tests from a clean slate.

Conflicts, serialization, and deployment dependencies appear as soon as we use this strategy. The environment
becomes a shared resource, and it causes friction among teams as once a new deployment is complete, it will
replace the state and data that was there in the pre-production environment.

#### Production environment

By deploying in production we can just test the feature on-live. This is done by setting the new feature
under a feature flag, so the old behavior is preserved unless we decide to do the updated way.

Sometimes it is difficult to implement this change with feature flags, because maybe the change is
destructive and affects to several parts of the service, rendering several of them unable to work as they were.

The test is done by setting a flag and running a the operation via a headless browser.

The hardest part is not toggling the feature flag, but making the software so resilient that in case
of an update of the data in any of the data stores, the application does not crash.

### Limitations of testing on the cloud

There are several problems with running the tests on a cloud environment: consolidation of architectural 
mistakes and cost.

#### Consolidation of architectural mistakes

First let me explain that when I say *test the design*,
I do not only mean testing that the design is correct, but that it performs well,
and scales well. Just throwing money to a problem in the cloud can solve any issue you find, but
that is not the way to do it.

As you cannot really test the architecture before having all deployed in your cloud provider,
a mistake in the design becomes permanent.

#### Cost

At the end of the day, running in the cloud is going to be more expensive than running in your local.
You are paying processing capacity, memory, data storage, and transfer. Maybe it is not much for a test,
but if your architecture comprises hundreds of services, and you need to keep an environment just for
testing, you are effectively doubling your cloud bill.

In another words: **your infrastructure works fine, but at what cost?**

## Testing on a locally simulated stack

The solution for this is to first create the infrastructure in your machine and run tests on the
architecture too. Check that the communication among services happen, and even take measurements.

### LocalStack

[LocalStack](https://www.localstack.cloud/) is a company that provides a docker image with the
services that behave like the AWS ones, even portraying the same API! So you can just replace
the connection details, and use them as if it were the real ones.

#### Example

I have implemented[^2] a [docker-compose.e2e.yml](https://github.com/diegojromerolopez/isidorus-web-scraper/blob/main/docker-compose.e2e.yml) in my Isidorus Web Scraper project that contains all
the services that I use in production: S3, DynamoDB, and SQS. This has helped me to understand
the relationship among them, and how I could scale my services depending on the load.

In the GitHub actions of this project, there is [an E2E workflow](https://github.com/diegojromerolopez/isidorus-web-scraper/blob/main/.github/workflows/tests-e2e-basic.yml) to ensure that the basic E2E tests are passed
before allowing the pull request to be merged to the default branch main.

### Custom replacements

The AWS services have been in the open for a while, and there are many open-source projects with docker images
that are publicly available and that you can use it to check the behavior locally.

#### Example

I have implemented a [docker-compose.prod.yml](https://github.com/diegojromerolopez/isidorus-web-scraper/blob/main/docker-compose.prod.yml) with different services that have the same API than the
ones from AWS, but that are built by the community instead of being managed by AWS. So I could run them
locally, understand how do they behave, and even deploy it in an agnostic cloud![^3]

I used the following replacements for AWS services:

- [Minio](https://www.min.io/): replacement for S3.
- [ScyllaDB](https://www.scylladb.com/): replacement for DynamoDB.

I indeed called this docker-compose.yml file with the infix *prod* because by using [kompose](https://kompose.io/)
I could create a kubernetes description of the infrastructure. Yes I had to touch it and modify things like
scalability, but I achieved a completely agnostic infrastructure that could run in any cloud provider that
accepted kubernetes. [See it for yourself](https://github.com/diegojromerolopez/isidorus-web-scraper/tree/main/k8s).

## Conclusion

Using your cloud to test functionality is not the best solution. Create local infrastructure and stablish
a baseline on performance and functionality.

Using local infrastructure will help you understand better the system design and how communication is
spread through your project.

Beware being locked-in by your cloud provider. Not only it limits your potential growing, it can be a death
sentence if the costs are increased by the vendor.


[^1]: master or main, meaning your default branch.

[^2]: yes I have used LLMs for creating the Isidorus project.

[^3]: It is not the point of this post, but the vendor-lock in is real. Coupling your project to a vendor is a grave mistake. You are a captive of their policies, and if they decide to increase your bill, you cannot do anything. Migration to other provider can be impossible because the changes are innumerable.