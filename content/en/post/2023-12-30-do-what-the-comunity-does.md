---
title: Do what the community does
date: "2023-12-30T00:00:00+02:00"
draft: false
tags: ["software", "community", "culture"]
---

# Do what the community does
The other day I had a conversation with a team mate about
how to implement different patterns to solve a common issue
in a interpreted programming language. He was sugesting using
a pattern not used at all by the community that indeed was
a cool, interesting, and *we could argue that* it was a more correct one.
**I was against that**.

## Humans are gregarious and tend to form communities
... even programming language communitites! And they
develop their own culture for years and years, being
unique and different than the ones from other languages!

## The perfect is the enemy of the good
... and there is no magical hammer that converts everything
to nails. Including a solution that feels *foreign* to
a programming language is going to feel forced. If the
community does not use the language that way, it is
because for years they have tested several patterns
and decide that (for the features of the language)
there is a set of patterns that are adecquate for it.

## What about experimenting new things?
... experiments are not part of the standard production
of features. They are needed when there are some *unknowns*,
but we cannot make projects be based on experiments.

If you want to experiment, go create a pet project and broke
the community rules, try it out and see if it feels *natural*.

But **do not do it in a production project**.

## Your code will be read for others developers
... even when you are long gone. Relying on community rules and
styles makes the code easier to deal with. Less time spent on
extending or maintaining it means faster development and release
of new features.

Besides that, developers would not have to adapt to a different
style/set of paradigms if the codebase follows the guidelines
from the community, so the onboarding process of new members
would be faster.

## Conclusion
While tempting, in production projects, be *conservative* and
use what has been working for a while. Do not apply patterns
that have no place in the language.
