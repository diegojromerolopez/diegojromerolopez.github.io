---
title: Out of the tar pit
date: "2015-08-25T00:00:00+00:00"
draft: false
tags: ["software engineering", "papers", "imperative programming", "declarative programming", "functional programming"]
---

"Tar pit" is an idiom used since 1970s based on the similarity between software complexity and tar pits trapping engineers and animals (resp.).

[Out of the tar pit](http://www.shaffner.us/cs/papers/tarpit.pdf) is a paper that analyzes the causes of this complexity and classifies it in several categories. The authors also analyzes the approaches that each type of programming technique uses to sove this complexity problem.

But the most important contribution the authors do is giving a solution in the form of a new paradigm of computer programming. They show a declarative language based on Relational Algebra invented by E. Codd that solves the inherent complexity that plagues the imperative languages code we use everyday.

This technique is called Functional Relational Programming by the authors and is based on:
- Functional programming.
- Not making differences between values and relationships (called relvals).
- Defining inherent constrains for the system.
- Having derived relations that contains the logic of the system.

I'm amazed by the simplicity and clarity of this approach, like other declarative languages like SQL, not having to worry about how is it done and only about what do I want is perfect for large software systems.

Authors Moseley and Marks are worried about performance but in my own experience of developing web software platforms, performance is the last problem among the developing of the software. Most of the time problems arise when clients change requirements through the life of the project and we have to delete and refactor code because these requirement changes are not consistent with our solution. Of course agile project management helps with that but the complexity, the bad code and the shortcuts keeps growing until a refactoring is needed.

I'm sure Functional Relational Programming systems can free the developer from menial tasks and help him/her center in the functionality the same way SQL almost completely frees us when dealing with the storage of our project data.

