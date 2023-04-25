---
title: Bike sheding in merge reviews
date: "2023-04-26T00:30:00+02:00"
draft: false
tags: ["software engineering", "code reviews"]
---

# Bike sheding in merge reviews
Focusing on the important things is a crucial matter.
When trying to solve a problem, sometimes we
subconsciously focus on the *easy* part,
the known part, the part we know we can tackle,
and forget about the *other* parts. The hard parts.

## Prelude
*Humans are falible, we know that we are not as
rational, impartial and intelligent as we like.
We are full of flaws.*

### Bike sheding
*There were the best minds in engineering. Their
mission was to build a nuclear power plant.
They had 12 months to do it. That power plant
would have to had (among other things) a bike
shed. The engineers used 80% of their time
designing the bike shed instead of designing
the hard parts: the actual nuclear power plant.*

More or less, this is the story a team mate told me today.

I suppose the story I just wrote is an apocryphal tale,
however the term *bike sheding* exists and means
focusing on the not-important part subconsciously.

### Electrons
*The electrons are like the bad students, they always
take the easy way* said one of my teachers. Well,
not only the electrons are like the bad students
(and viceversa), almost everybody behaves like an electron
and if not, that person is considered an *outlier*.

## Bike sheding in code reviews
Let's stop with the metaphors and *ethereal* examples.
Software Engineering is a vast discipline, and some
of its contents are not standardized. One of this
parts that is more related to heuristics than with
mathematics is the code review process.

As the reviewing process depends on the humans,
they tend to suffer form our *falibility*, including
bike sheding.

Can we set a set of rules to minimize bike sheding?
Let's try

### Understand the change
To do a code review it is not enough with
reviewing the code. You have to understand the
change, see the flow running and check that
efectively, the feature (or fix) makes sense.

### Focus on what you do not know
While reviewing code, don't focus in what you
understand. Try to understand what you don't
understand.

Forget about the style, get information
about the *intent* of the creator of the pull
request. Get information about *what is expected*
of the pull request.

I tend to run the test step by step and see
the code running in my IDE. Sometimes, if
possible, I like to run the code locally
and test it by hand.

My point is that by playing with the feature,
you are learning about it and getting an
image of what it is. The question is not
if it the changes are OK? You should be
asking yourself if the changes are enough.
Is the feature complete? Are all the cases
take in account?

### Go deep
Does it make sense to review the code style only?
Checking that the code is more-or-less well structured and
tested? No, of course not. Treat a +1 as a badge of honor.
If you need an explanation of a part of the PR, ask for it.
If you don't receive the explanation, don't give the +1,
simple as that.

Don't comment on things like style or structure
unless you perfectly understand the changes.

## Conclusion
Our subconscious guide us to known paths, even during the
code reviews. Fight agains it, and do full code reviews,
understanding fully the change.
