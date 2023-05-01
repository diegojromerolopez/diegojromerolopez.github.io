---
title: Code reviews or understanding the code
date: "2023-05-02T00:00:00+02:00"
draft: true
tags: ["software engineering", "code reviews"]
---

# Code reviews or understanding the code
How would you do a code review? Only by reading the code
changes or do you thing you need to actually run the code,
and what is more important, fully understand the
modifications?

## A tale of two code review cultures
Let's compare the two following environments:

### Slow but safe team
Imagine a team were reviews are done by several members.
There is a focus on the detail, PRs are slow to be merged as they are
improved several times before the final merge.

Most of the time, the original developer must convince the reviewers
that some of the implemented solutions are fine. Besides that,
**the code is run and showed to the team**.

The software the team produced is not critical but is treated as
such. You can image the velocity of the time is not high, but
they last incident happened... never.

### Fast and dynamic
PRs tend to be small, reviews only are done by analyzing the code
style and running the code inside the heads of the reviewers.

If the language uses dynamic typing, the code relies on tests,
but in the tests you are assuming the mocks are done well and there
are no hidden issues.

Velocity is high, reviews do not lasts more than a couple of hours.
You can ask somebody to review the code and that developer is going
to give a positive review with a 90% of probability (unless there is
a very explicit mistake in your code).

What is going to be the rate of issues when adding new features to
the code base? You guess it... High or very high. Most errors are
detected after deployment.

## Conclusion
*Dress me slowly, I'm in a hurry* could be a good way of summing up
the ideas of this post. Sometimes slow processes are good because
they are *battle-tested* and produce *ironclad* products.

It is better to have a pull request waiting for reviews for days,
or show the code running, and then receive high-quality feedback,
than passing your PRs with honors, only to find errors in the
deployed environments.
