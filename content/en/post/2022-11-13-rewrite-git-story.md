---
title: Rewrite git branch history
date: "2022-11-13T00:00:00+00:00"
draft: false
tags: ["git", "rewritting", "commit"]
---

# Rewrite your git branch history

Ever had a pushed branch that is completed and ready for review but the git
history is too long and full of commits with bad messages? This post
gives you a way of solving this.

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
git reset
```

This command will out all your changes from the stage, hence preparing all
files for being added commit by commit by you.

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

Once you have all new commits ready, push all your changes:

```sh
git push --force
```

The `--force` is neeeded because we have to rewrite to remote branch.

# Conclusion

Do not pay attention to making good commit messages or to divide your work
in commits. You only need to know some commands
to rewrite the history of your branch posteriorly.
Hence, you can get a clear and
meaninful commit history, ready for the your team mates' review.
