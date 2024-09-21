---
title: The long silence
date: "2024-09-21T00:00:00+02:00"
draft: false
tags: ["metapost", "updates"]
---

# The long silence
It has been some months since I wrote here for the last time.
Why have I been silent all this time? I could say that life
matters have made me pretty busy (and that is true), but
apart from that, what things have I been working on?

## Things I worked with

### Deno

[Deno](https://deno.com/), the next-generation JavaScript runtime created by Ryan Dahl,
the Node.js creator.

It think it is a great idea but it has some rough edges, let's hope that with the
coming of [Deno 2](https://deno.com/blog/v2.0-release-candidate) and the full support
for commonJS modules and other new features it can achieve the status it deserves.

### Deno fresh

[Deno fresh](https://fresh.deno.dev/) is a convention-over-configuration web
framework *à la* next.js, and it is a delight to work with.
Creating a simple web service is as easy as it could be.

Based on [JSX](https://en.wikipedia.org/wiki/JSX_(JavaScript)) and emenentily
oriented to server-side rendered components, it also features islands,
that are pieces of client code that will be delivered and run by the browser.

However I am encountering some issues with the Islands, mainly they do not load
under certain cirtumstances. More on that in subsequent posts.

### Typescript

Of course as Deno's main language is Typescript (although it is compiled
to Javascript under the hood), so I needed to remind my previous experience
with this typed language from Microsoft.

I would say that the types are useful for understanding the code, and that they provide
a good way to improve the overall developing and maintaining experience.

However, if you encounter an issue with a library were it returns
an object of a different type than it should, you are not warned at all.
I mean, there is no type checks at runtime.
So it is more like a glorified type hinting mechanism
(as Python does have it).
Of course that was the aim of Typescript as it is compiled to Javascript,
but I wonder if a *type-safe* mode
where the compiled javascript code is type-checked could we of interest.
Having this feature could enable some pre-production systems
to be easily debuggeable.

Nice language, I find myself missing it out when working with Ruby.

### Ruby

I work daily with ruby, so nothin spectacular about this. However, I read some
months ago the [rspec best practices](https://github.com/abinoda/rspec-best-practices)
and I have applied those practices when writing rspec tests.

Mainly I would say that the ones that have had more impact in me had been:

[Use context](https://github.com/abinoda/rspec-best-practices?tab=readme-ov-file#use-context):
it is not a secret that my background is in python and that unittest tests are not implemented
in a [BDD](https://en.wikipedia.org/wiki/Behavior-driven_development) manner,
as [rspec](https://rspec.info/) does, so most of the time
I just ended up defining the behaviour in the `it` block descriptions.
That is wrong! You should use the context and group the cases as
if every context was a condition! the it block descriptions should
only reflect on what happens because of the logic of the piece of code
that you are testing. Of course a lot of tests were rewritten because
of this.

[Only one expectation per example](https://github.com/abinoda/rspec-best-practices?tab=readme-ov-file#only-one-expectation-per-example): because I tended to have gigantic
tests with a lot of assertions. Does this feel like helping understanding the behaviour
of the code? No, I do not think so. So just by checking different expectations you help
maintainers a lot, more even so, if you include edge cases in different tests.

There are a lot of practices that are interesting and can be applied,
like the DRY principle, where reusing code via helper methods
(or shared examples I would say) is encouraged.
This also happens to be in frontal opposition with my last 3 years
of Python development, where the tests where all big chunks of code
where almost no other function than the tested one was being called.
I think this example ilustrates the different cultures of the
programming language communities.

### Python

Well yes, my old friend. I have been working with the
[slack bolt framework](https://github.com/slackapi/bolt-python).

It is funny how after yo work with different programming languages you miss some features of
one in others. In this case, I dislike how tests are implemented in Python with unittest.
I prefer how Ruby's rspec deals with mocking than the unittest mock.
But I will explain more in depth in other post.

Apart from that, not much. Python continues being Python,
but I am excited about the release of
[Python 3.13](https://docs.python.org/3.13/whatsnew/3.13.html)
where there is
[an experimental non-gil mode](https://peps.python.org/pep-0703/).
What could I implement with this? I wonder.
As concurrency is going to be a first-citizen in
Python, what could we work on? Need to think about this.

#### Gelidum

Some days ago I discovered that there are several interesting users of my Python library
[gelidum](https://github.com/diegojromerolopez/gelidum),
as seen in the [dependents](https://github.com/diegojromerolopez/gelidum/network/dependents)
page of the github project (spoilers: Microsoft CCF).

I always do my open source contributions with the intent of
being useful for others, helping the community
and overall, helping the humanity. So I hope that the users
of gelidum have had a good time using it,
have had a good time using it, and find
it useful (I'm always open for feedback).

### Domain Driven Design

Well, yeah I started reading the
[Learning Domain-Driven Design book](https://www.oreilly.com/library/view/learning-domain-driven-design/9781098100124/)
by Vlad Khononov because I feel disenchanted with how I have
been structuring my software projects along the years. The book starts with an explanation about domains
and it is refreshing to

I have refactored a project to follow the DDD guidelines (more or less)
and have had to leave the domain
layer out, as the data objects where all along the place.
While this is not ideal, I have achieved some
order in the codebase, and having data repositories, external sources,
configuration and other infrastructure
elements contained *is a bliss*.
I will write some more about this experience.


# Conclusion

3 different programming languages and a new software architecture style,
not bad so far. I hope that by end of the year I have completed Khononov's book,
and can apply DDD fully and from the begining to a new project.
