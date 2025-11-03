---
title: Use Static Single-Assignment when possible
date: "2025-11-03T00:00:00+02:00"
draft: false
tags: ["programming", "quality"]
---

# Use Static Single-Assignment when possible
This post discuss a way of coding assignments in code where
all variables are treated as constants.

## Introduction
There are simple ways to improve our source code that are simple but effective.
Static Single-Assignment (SSA) is one of them.

By changing the way variable assignments are done, we can achieve some
benefits in maintainability that cannot be overlooked.

## What is Static Single-Assignment?
Just treating the variables as constants, i.e. do only one assignment per variable.

The term SSA comes from compiler design, where SSA acts as an intermediate language
that the original source code is compiled to.

This SSA is also present in [functional programming](https://www.cs.princeton.edu/~appel/papers/ssafun.pdf), as there are no variables in functional programming languages, but references to values
(well, sometimes they are called variables, but they are *constant* values).

### Examples

Let us see a *toy* example:

```python
x = 2
x = x * 2
```

The overwrite of x clashes with the SSA, it should be rewritten as:

```python
x = 2
y = x * 2
```

The best way to enforce it is to use the programming language capabilities (if they exist):

If the language has the const keyword (like in TypeScript), you should use it:

```typescript
const message = condition ? "Message A" : "Message B"
```

Or for languages (like Python) without a const keyword but some static checks,
you could use those:

```python
from typing import Final

message: Final[str] =  "Message A" if condition else "Message B"
```

Of course, in the case of Python I would say that almost anybody uses Final this way,
as it could "pollute" the code.

## Limitations
What about loops? Yo cannot do anything there, you need variables to be updated
there, so you cannot apply SSA to them.

However, I always suggest marking the variable in a way that is clear that is updated
in the loop, and is not a constant value like the others.

## Advantages
The code needs to be readable by humans,
and this technique provides a lot of benefits to the source code: better
readability, understanding, and debugging.

### Avoidance of mistakes
Your code modifies a variable once and only once. The coding errors
not only are apparent, but easy to identify and fix: just checking the usages
of each variable can give you the *culprit*.

### Better understanding
It is easier to understand the code. You can trace the flow and
even trace back with just a glance. Each variable represents a part of the
states that were needed to get to the end of the functionality.

### Better debugging
Debugging is also improved. Once you see a variable being assigned,
you do not need to worry about it being updated in other flow.
You do not need to beware side-effects of other flows changing the value.

This decreases the mental load of the developer
while debugging a piece of code.

### Better observability
Because of the better tracing obtained by using this technique, you can also
improve the [observability](https://glossary.cncf.io/observability/)
capabilities of your application, by sending all the changes of state to our
telemetry provider.

By having only a value assigned per variable, we can make sure that when we send
the variable to our telemetry provider, that is the only value that we need to
send.

## Disadvantages
Not everything is good, I am afraid. Sometimes we need to create
code that is difficult to understand for performance reasons.

### Changes in existing codebases
It is a low-level change (not much difficult to do), but it is difficult to
apply on existent codebases. What can you do with a project of thousands of
lines of code that re-uses the same variables again and again?

We cannot expect to change all the code to make it follow this pattern.
It does not make sense. The changes should be applied function by function,
class by class, and module by module.

### More resources are used
Re-using variables could be reduce the memory of an application,
as we would not be storing *removable* information.

Apart from that, some performance improvements could be obtained
for having less variables to be checked by the garbage collector.

However, in most cases, the performance gains are tiny, and unless
you need a more performant software, you should not optimize your
code by re-using variables.

## Conclusion
We have shown why we should be using SSA in our code, and how this
simple and low-level technique can improve the quality of your code a lot.
