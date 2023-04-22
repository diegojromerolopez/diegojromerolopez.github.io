---
title: Git History in PRs
date: "2023-04-22T00:00:00+02:00"
draft: false
tags: ["software engineering", "git"]
---

# Git History in PRs
Suppose you have a big feature, and you are creating
a pull-request with all your changes. How do you
organize the changes? Only one commit? One per sub-feature
or sub-fix? How do you make that division? Or maybe you
could organize the commits in a way that is helpful for
reviewers... But how? This post try to show different
approaches I have found during my years in the workforce.

## Alternative 1: hard semver
In this model of work, the PRs do not matter,
the git history does not matter, only the versions matter.
i.e. the history of the commits is not examined at all.
The version of the project is what is important, no PR
reverts are made, only forward modifications.

In my opinion, this is a prehistoric way of doing things.
While of course in the case of an issue the version only
moves forward, not relying in the git history is making
yourself (and your team) a disservice.

## Alternative 2: smaller PRs, the git history does not matter
Sometimes combined with the *hard semver*, this way of working
tries to have small PRs that could be understood by simply taking
a look at them. Not having to go step-by-stem, i.e. only visiting
the *changes* section of the PR.

The good thing of applying small (hence incremental) PRs is that
if an issue arises, reverting them does not cause a *pain* to
users, developers and other teams. Maybe the main functionaly is
here but an edge case (that happens with a less than 1% chance) was
causing an outage, so reverting the PR that modified the functionaly
for fixing that 1% is *safer* that if we would have to revert
a PR with the full functionality, with dependencies wit other
functionalities, etc.

You know what they say: *incremental improvement is the king*.

## Alternative 3: big PRs, one commit, the git history does not matter
Remember that we are talking of making easier the life of the
reviewers, not understanding the full history of the *master*
branch. However, what about [~~ab~~using git to rewrite your
git history](/blog/2022/11/rewrite-git-branch-history/)?

Some like that, some not. I think it all depends on the size of
the PR. If we are talking about a small PR, it does not matter.
If there are hundreds of changes in your PR, and there is only
a *lone* commit, how do you start reviewing such a big change?
It is difficult to tackled a PR so big without any indication.

In the case of a big PR where the history does not help, we
are going to ask for a *show and tell* session.

## Alternative 4: the git history of the PR matters
In this alternative, the PRs can be enormous or tiny, it does not
mattter, really. The code reviewers are going to go commit by
commit reviewing the changes incrementally. So you need to group
your changes accordingly so.

It does not matter if there are 20 commits as long as they are
logically independent and the reviewers can go step by step
reviewing what would be your work (more or less).

This is a good way of doing things. git provide us with functionaly
to check and rewrite history, why don't use that?

## Alternative 5: show and tell
Most of the time this is not an alternative, but a core part
of the code review. Instead of torturing your reviewers trying
to understand what your code does, **show the changed code running**.

Of course they can also review the minor details of the code, see
if it works for all *edge cases*, it is secured against possible
issues of malicious users, etc. but by explaining the code you wrote,
you do most of the heavyweight work for them, and leave only pure
software engineer review details for them.

Combine this approach with having a *sane* git history of the commit
and *you are golden*.

## Conclusion
Use the tools that git provides to create good PRs. Provide a
easy-to-follow history that helps the reviewers go commit by
commit **understanding your thought processes**.

Besides that, adding a review meeting with the reviewers
is going to be appreciated for them (and actually also by you),
as the conversation about the PR is going to be faster and seamless.
