---
title: Rewrite git branch history
date: "2022-11-13T00:00:00+00:00"
draft: false
tags: ["git", "rewritting", "commit"]
---

# Rewrite your git branch history

Ever had a pushed branch that is completed and ready for review but the git
history is too long and full of commits wit.

# How to

The process is very clear. You only have to get the changes, move your point
to the branch you want to merge (usually *master*), unstage everything,
creating new committs, and force push the changes.

Let us see the process step by step:

## Revert all your commits

Assuming you are in a branch and want to do a clear history with respect to
the *master* branch, the first step is doing:

```sh
# Note that if you are creating a pull request against main, you will have
# to use the branch main instead of master
git reset --soft master
```

[This command](https://git-scm.com/docs/git-reset) will reset your
head to master, but will keep all of your changes in the stage.

## Unstage everything

```sh
git restore --staged .
```

This command will out all your changes from the stage, hence preparing all
files for being added once again to the stage commit by commit, but this time
with a *beautiful* and *meaningfull* history, by you.

## Add and commit as you wish

For each group of files you want to add to a commit, add them to stage
and make a commit:

```sh
# Assume there are modifications in file1.rb, file2.rb and file3.rb
git add file1.rb file2.rb
git commit -m "feat: new feature that is exciting"

git add file3.rb
git commit -m "fix: file 3 had a bug"
```

## Push your modifications

If you type now `git status`, you will get a message about that your branch
and the origin branch have diverted. So you have to force the change with

```sh
git push --force
```

The `--force` parameter is what causes the remote branch rewrite.

# Conclusion

Do not pay attention to making good commit messages or to divide your work
in commits. You only need to know some commands
to rewrite the history of your branch posteriorly.
Hence, you can get a clear and
meaninful commit history, ready for the your team mates' review.
