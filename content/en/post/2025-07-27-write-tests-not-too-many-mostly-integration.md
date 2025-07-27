---
title: Write tests. Not too many. Mostly integration.
date: "2025-07-27T00:00:00+02:00"
draft: false
tags: ["software", "testing", "reflections"]
---

# Write tests. Not too many. Mostly integration.
This is some advice that appear first at Twitter by [Guillermo Rauch](https://rauchg.com/).
Years have passed since I read it and now I am at a position to reflect on them and how I
was following this advice even when I did not know that *explicitly*.

## Introduction
Some years ago I was developing an internal web application for a non-*techie* team.
I was working with React and reading a lot of tutorials, guides, and documentation
(in case you are wondering I was mostly focused on backend those days).

Some of the pain points where related to the creation of tests in React with the
[react-testing-library](https://testing-library.com/docs/react-testing-library/intro/),
so I was reading a lot the blog of [its creator](https://kentcdodds.com/blog/common-mistakes-with-react-testing-library): [Kent C. Dodds](https://kentcdodds.com/).

One of the posts I read in Kent's blog was
[Write tests. Not too many. Mostly integration.](https://kentcdodds.com/blog/write-tests).

The post did not make an immediate effect, but I liked the idea, to have some
*foundational* tests, *relatively* easy to do, and run,
and that they could detect an error in the functionality.

I was working for a big corporation, with a focus in quality and detail, so
I was *obsessed* by testing, as a way to stop possible errors in the implementation
reaching to the QA or eventually the user.

I had worked for a while with testing, but I was not skilled enough in doing
frontend tests, so I was learning and improving my craft *non-stop*.

## When testing is important?

Testing is always important, the complexity that we face cannot be tackle unless
we have some assurances that the behavior is fixed and correct.

## Are integration tests more important than unit tests?

Integration tests are those that do not mock more than needed.
As Kent writes it very eloquently:

> Regardless, I think the biggest thing you can do to write more integration tests is to stop mocking so much stuff. When you mock something you're removing all confidence in the integration between what you're testing and what's being mocked. I understand that sometimes it can't be helped (though some would disagree). You don't actually want to send emails or charge credit cards every test, but most of the time you can avoid mocking and you'll be better for it.

I would say that by having tests that
[mock only the absolute minimum](https://diegojromerolopez.github.io/blog/2025/06/the-testing-pyramid/#integration-tests),
you are guarantying that big parts of the system behave as expected.

And what is this *minimum* part you need to mock?
**You should be mocking only external dependencies that we have guaranteed to behave in an expected way**,
i.e. most of the time packages with good support from the community.

In the case of not relying on a package, but raw service with the communication layer, we should mock that and treat it
as a project dependency even if we have created it.

## Should I start working with integration tests?

In my experience, integration tests tend to be more useful than unit tests before the project reaches a stable state.

The codebase is going to suffer big refactorings for sure in the immediate future,
so if you start creating unit tests, you are going to need
to rewrite those once you are done with the expected refactorings.

So yes, you should start with integration tests. Now... It is not always possible to mock
everything in an easy manner so you will need to rely on mocking more parts than the dependencies.
For example, this happened to me when I was working with a ChatOps bot done with the
[Slack bolt Python framework](https://github.com/slackapi/bolt-python), and testing
the reception of a message was not an easy task
(I ended up [creating a small library for testing with Slack bolt](https://github.com/diegojromerolopez/slack-bolt-testcase)).

## Could not just rely on unit tests?

No. Unit testing enforces the contract between the different layers of your application,
so you could have 100% unit testing coverage and have failures in your project.

**When you are mocking everything you are testing nothing**.

Unit tests are useful for ensuring the communication among modules is done in a certain way.
Nothing more, nothing less.

## Should we just rely on end-to-end tests instead?

No because end-to-end tests are usually more difficult to implement, maintain, and run.

End-to-end tests are implemented via mock servers. So a change in the protocol need a change
in the server, and that is more work. Those mock servers can be based in other technology,
or required a new release in other project.

End-to-end tests are slower, they rely on starting up entire services so usually you only
run them in your CI/CD pipeline, not locally.
**Slow tests tend to not be run as frequently as they should.**

## Should then stop doing so much tests?

Well, in my experience testing coverage does not guarantee that there are no errors,
but having a low testing coverage is usually a symptom that there are *bugs* in the code base.

I do not think we should do tests for the sake of having tests, but you need to keep this in your mind:

- Integration tests check functionality.
- Unit tests check relationships.

So once you have ensured the functionality via integration tests, and once the design is all set,
you could do unit tests for the rest of the code base.

Hence, in a refactoring you will encounter failing unit tests but (ideally) no failed integration tests.

## Final remarks

### I'm not getting paid for creating tests

Then find another job.

Quality is not negotiable, if your manager asks you to stop adding tests for your code,
then you are in the wrong place. Software is not only source code with features,
but documentation, and tests.

### Could not LLMs tell us if the code is right or wrong?

No. The Large Language Models (LLMs) fail to work when the context is large or .
They are useful for autocompletion, small refactors or other use cases, but
they tend to do some small tweaks in the code automatically, 

Apart from that, remember that **LLMs do not have a fully expected outcome**.
So a change in the model, the context, or the meta-parameters can make the
LLM to produce a different output.

**We need stable, and reproducible checks for our code.**

### Isn't this work for the QAs?

No. QAs could do manual or end-to-end testing or whatever tests they decide to do,
but it is not related to the work we do.

By having a separate validation process, we ensure the QA team is not influenced in
any way by the decisions that software engineers took.

**How many times you have forgotten testing the edge cases?**

**Quality is a responsibility of the software engineers**.

## Conclusion
Read the [full blog post from Kent](https://kentcdodds.com/blog/write-tests),
it is short and contains a lot of wisdom. You do not need to be a frontend engineer
to understand it, nor to apply it in your day to day tasks.