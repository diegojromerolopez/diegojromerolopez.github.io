---
title: Add changes to your last commit
date: "2022-11-16T18:36:00+01:00"
draft: false
tags: ["git", "rewritting", "commit"]
bigimg: [{src: "/img/corrections.png", desc: "Some corrections on a Manuscript (from https://publicdomainreview.org/collection/a-closer-look-at-richard-wagner-s-manuscripts)"}]
---

# Add changes to your last commit

Have you ever created a commit with a meaningful message and,
later wanted to add or modify something to it? And what about if you pushed
that commit? Here we are going to see how you add changes to a commit,
independently of if it was pushed or not.

# How-to

Let's suppose we have just pushed a commit and we want to add
another change to it. This process is called
[amend](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---amend).

Let us see the process step by step:

## Add changes to stage

Add the changes to stage:

```sh
git add file1.rb file2.rb
```

## Amend the commit

Add changes to commit:

```sh
git commit --amend --no-edit
```

In case we want to modify the message type

```sh
git commit --amend -m "New message"
```

## Push your modifications

**(Only if you pushed the last commit)**

You can type `git status` and see how your branch and the origin branch
have diverted. As we did in [the previous post](/blog/2022/11/rewrite-git-branch-history/), you have to force the push moving the
remote head of the branch.

```sh
git push --force
```

The `--force` parameter is what causes the remote branch rewrite.

# Conclusion

Do not worry if you have to add more changes to a commit,
*it happens to all of us!*. Use amend to fix the last commit
and *that's it!*.
