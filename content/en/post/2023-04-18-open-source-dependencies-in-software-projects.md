---
title: Open Source dependencies in software projects
date: "2023-04-18T00:00:00+02:00"
draft: false
tags: ["software engineering", "open source", "dependencies"]
---

# Open Source dependencies in software projects
Most of the foundations of current commercial software
projects are open source. But what happens when an
open source project becomens unmaintained?

## Dependencies, dependencies everywhere!
Most software projects have a miriad of depedendencies.
Why? Because we (as software engineers) are not going to
reinvent the wheel. Having your software depend on a
well-tested, maintained, and supported is a bliss. It
saves you time, and work very easily: you only have to
be aware of two things:

- Breaking changes.
- Updates because of bug fixes.

Of course we have to reach a balance. We are not going to
develop everything from the ground up, but we are not going
to only *join* different libraries (well, sometimes it is not
much more than that!).

## Open source dependencies
Most of them are open source. The reason is simple. There are
millions of open source projects that fulfill a need, are
developed in the open, and have a compatible license.

If open source would not exist, we should have to develop
everythin in-house, falling in the pit of despair of having
to maintain thousands of internal projects just for a small
client-facing project.

We do no think enough to the open source contributors for this.
And that brings me to the following point...

## What can you do if one of your open source dependencies is unmaintained?
In this scenario, your project has a dependency on an open source project.
The maintainer (the main developer of the project) has stopped working on that.
Bugs are starting to appear, maybe  some incompatibilities with other packages
have arise, or even worse, the package does not work anymore with the last
version of its programming language.

### Solution 1: fork the open source project and maintain it
This solution seems to be the recommended one by github with its wonderful
feature *fork*. You can copy the project in your github profile and
appy the changes you need to make it work.

Of course, the problem sometimes is that you are not the only one that
has forked the project, and can be in a situation where there are thousands
of forks of a project, with different standards of quality: some of do not even work.

Are you going to redo all the work someone has already done? But has that developer
done it well? And the worst question of all, among the thousands of forks, which
one is the one that fit your use-case better?

### Solution 2: search for another package with the same dependency features
Title says it all. Search for another package that fulfills the same
need and replace the old with the new. This is could be a hard task,
requiring rewriting almost all of your project.

I do not recommend this solution. Having to rewrite all your code that
calls the dependency, having to change flows to adapt them to the
new dependency, hoping to do not have any kind of incompatibility
between your current dependencies and those from the replacement...

The possibilities of new issues arising are *more than a few*.

### Solution 3: become an official maintained of the project
This is my favorite solution, maybe not the hardest one from the
technical point of view, but not an easy way-out from the issue
either. Having to deal with project management, angry users and
of course, having to fix every bug that happens when its dependencies
or language require, is a lot of work.

However, the good thing is that you are going to collaborate with
the community and sometimes, the community helps you: issues,
bug reports, feature request, suggestions, full PRs, etc. Do not
underestime the work of your new users, as they are indeed
developers.

## Conclusion
If you encounter with the scenario of having a project depend on
an old package, try to become a maintainer. You will be helping
the community and also getting help to improve the package.
