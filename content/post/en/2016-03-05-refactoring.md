---
title: Refactoring
date: "2016-03-05T00:00:00+00:00"
draft: false
tags: ["software engineering", "refactoring", "programming"]
---

# Introduction

Software is not a static element in a business. It evolves as business needs evolve. How can we make changes in software and keep high quality or, even better, not degrading it as we develop functionality?

# Refactoring

[Refactoring](https://refactoring.com/) is the process of changing code structure for the better while keeping the same functionality. It should be a continuos activity made during software development, with the aim of easing maintainability of software.

The main aim of refactoring is having a simpler software design, increasing its understandability and therefore, making easier software maintenance and extension.

# How can I learn refactoring?

Martin Fowler[^1] wrote a compendium of known refactorings: [Refactoring](https://martinfowler.com/books/refactoring.html)

The heuristics used to know when to apply a refactoring pattern is what he calls "smells of software". If the software stinks, you have to refactor it. Or in a more formal way, software smell is only one of the first common symptoms of fracture in the design of a piece of software.

In the same way a neighborhood starts decaying and its first symptoms one can find broken windows, garbage in the street, graffitis in the walls, etc. Software must be taken care when we detect bad quality code.

Thus, I really like the way Martin explains each pattern. Each one of them has a name, motivation and a description of how to apply it, step by step. There are also some easy examples to help you understand what means applying the pattern to a piece of code.

# How to refactor?

Changing code. As simple as that. Given we have a test that our bad quality passes, our aim has to be to apply the appropriate software refactoring pattern to make it pass too.

Of course, we can apply several of them in the process of refactoring, we don't have to be robots. One thing is for sure, our changed must be tested. Martin emphasizes the use of tests as a foundation of refactoring.

Why use tests? The test is what we use to assert that the refactoring does not break our software. If we don't have test, how can we assure software keeps working?

# Conclusion

Read Martin Fowler's book and then, read again and keep it as a reference manual.

As the software projects moves forward, refactorings will be needed to fix missteps taken during software development.

[^1]: Martin Fowler is one of the current giants of Software Engineering. He is a big defender of using microservice architectures and refactoring as tools to increase software quality. His [site](https://www.martinfowler.com/) has many Software Engineering resources and is a must-go site from time to time for me.