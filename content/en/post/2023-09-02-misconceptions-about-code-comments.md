---
title: Misconceptions about code comments
date: "2023-09-02T00:00:00+02:00"
draft: false
tags: ["documentation", "comments", "software"]
---

# Misconceptions about code comments
I have been working in this industry since 2008, and
it seems an idea is spreading through software companies:
code comments *are considered harmful*. Is that true?

## Where did all start?
I think that this idea started with the
[Clean Code](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)
book and the subsequent talks by [Robert C. Martin](http://cleancoder.com/products).

*Uncle* Bob (as people use to call him), has the idea
that code should be self-explanatory, and if there is a
comment, it is because code is not well structured. So the
code needs to be refactored, and then, the comment could be
removed as the code would be clear enough to be understandable.

His *magnus opus* Clean Code shows code patterns, examples,
and good practices to follow this rule. It is a good book,
with a good intent, and I should say it is a mandatory read
for all software developers out there.

## Non-comments cargo cult
*I am sorry if I sound harsh but prohibiting using code comments in a project is something that has happened several times in my career, and I think about this prohibition of cargo cult.*

Most clean code purists would detest comments because several reasons:
- Comments are not high quality enough.
- Comments must be updated.
- Comments are a syntomp of high complexity code.

While the ideas have some merit, they are falacies. Developers could
write high-quality *comments that actually serve a purpose*. Having a minimal
documentation in the code is needed for other developers to understand
the inner workings of the project. Relationships, behaviours, types,
how are a new developer understand this? Is he/she going to have a
long tedious onboarding?

Besides the points above presented, I like when code and design is linked
in some way. I am not opposed to documenting projects in external files,
but if there is no correspondence between the code and the documentation,
some time usually gets wasted finding the role of each part in the code.

## Tests as documentation
One counter-point to this argument of having tests in your code,
is that tests should show the behaviour of the code,
and make the comments unuseful.

As every possible control flow of the code is tested, if you do not
understand some behaviour, you can always go to the tests and see
it for yourself.

This is a good point, but encounters two difficulties: sometimes the tests
lack sufficient deep, and sometimes it is hard to test flows that depend on
several projects.

If the tests are only unit tests, you are going to have a bad time trying
to understand the flow of your application. If the next dependency of each
software module is mocked, how are you going to understand the full flow
of the application. Of course, with
[integration tests](/blog/2022/11/actual-integration-tests/) this could be solved,
or at least, mitigated.

But the other case is harder, how do you test a shared flow between a bunch
of services? Yes, you could argue that with a good end-to-end test you could
test the behaviour, but aren't you doing black box testing? How are you going
to follow the flow step by step through several systems? That is simply not
possible.

Hence it seems that, while tests are a must, some additional
documentation is needed.

## How to write good code comments
While I agree that most code comments tend to be not useful,
I am totally opposed to the idea of removing of all comments
as a hard-enforced rule. Most code are not useful because developers
tend to lazyness. If we are forced to write comments, we would
write bleak descriptions of function behaviours that are hard to read.
So we need to be diligent about that tendence.

Having said that, comments must be reviewed, they must be of high quality,
and must help developers. A comment that describes the next lines
is not a high quality comment, *why are you telling me the same twice?*.
However, a comment that gives context, a *raison-d'être*, gives a warning,
or explains some hard to understand behaviour is totally needed.

Second, if the language has no types, a good way to give some information
to future developers about the parameters is adding a wall of comment
before the function or class. Most readers would remember javadoc comments,
and the older ones would remember doxygen. In the case of ruby,
[rdoc](https://github.com/ruby/rdoc) is a must
as I would say this language's implementation of type hints is
(at best) controversial.

Third, comments and code must be in sync. Most *clear code purits*
I have met always defend their stance by saying that most of the
time developers do not update comments. Of course! That is why the
code reviews are in place. The team must review the comments and
the code, as the comments are actually part of the code
(as you would expect). Keep in mind this rule and you are golden:
*The worst comment is not the one that is missing, but the one that is wrong*.

And last, there are two classes of code complexity: inherent and accidental.

**Inherent Complexity** (IH) is the complexity the code has because it is needed
to fulfil the mission it has been created to. For example, a
multi-threaded code can be complex but there is no possible more simple
replacement. That is the way it is.

On the other hand, **Accidental Complexity** (AC) is the complexity we humans
*inject* in the code that is not neede to make it work, but we add to
the code because we are fallible. Of course a minimal accidental
complexity is OK, as it could help us understand better the code.

We need to tackle accidental complexity, but using code comments as a sign
that there is not a good idea as far as I see. Not because there is no
comments it means that the code has no AC, they are
completely two different (albeit related) things. Of course you could
argue that code with many comments have a high AC, but there is no guarantee
that that is true at all, we could have a high-AC code without comments,
simply as that.

The idea of different classes of complexity is not mine, and I borrowed it
from the excellent paper [Out of the tar pit](/blog/2015/09/out-of-the-tar-pit/).

## Conclusion
Relying on the presence of comments to evaluate code complexity
is a recipe for disaster. Enforce good code comment practices in your
team, and include the comments in the review process: they need to be
read, understood, improved, and if needed, updated accordingly.

## Post Script: but you have projects without comments!
Yes, that is right. One of my most simple projects (albeit useful)
projects have almost no comments:
[Gelidum](https://github.com/diegojromerolopez/gelidum)

But if you take a look at the code you will see that the flow is linear,
there are no dependencies in that project, and understanding that code
is a *no-brainer*.

Now, imagine a project with several services connected to the exterior
with different APIs and among them with a priority message queue. Would
it be enough to have a clean code or would you like some explanations
on critical modules?
