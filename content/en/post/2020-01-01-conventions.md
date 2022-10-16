---
title: Conventions
date: "2020-01-01T00:00:00+00:00"
draft: false
tags: ["software engineering", "career", "onboarding"]
---

*Conventions are what build our society*.

Nobody, but you'll get my point along this post.

# Conventions

## Write the code to make it obvious

Every software engineer develops an unique style of coding through their career. Usually they starts coding tangled code that is extremely difficult to understand to anybody but theyself. Later you get to the point where you are unable to understand your own code, and began to
wonder how is that possible. Later you get to the point where your code is obvious and easily understandable, it has no *tricks* and is... Boring.

You usually remove recursive functions (unless totally required), high order cognitive complexity, reduce the number of parameters, remove or encapsulate the state in objects, etc.

OK now your code is predictable and with a little of documentation can be understood by almost anybody.

## We don't work alone

However, when you work with a team you have to adapt your style to the *consensus* reached by the team.

For example you may develop functions with multiple output points but your colleagues development is inspired by the [NASA rules](https://web.cecs.pdx.edu/~kimchris/cs201/handouts/The%20Power%20of%2010%20-%20Rules%20for%20Developing%20Safety%20Critical%20Code.pdf) that mandate a simplified control flow and they interpreted them as only having a lone return in each function.

The point here is that although you may not be appreciative of this rules at first, they help the team reach a same standard of code. Thus, it avoid arid discussions about style, and allow the team to focus on features.

## Make conventions public

Conventions that are unknown by new team members will make them feel that their contributions are unappreciated. Every team must have a code style guidelines that are written in the project.

## Use tools to reach conventions

Humans are fallible and tools that re-direct bad code to convention-approved code must be in place. A good way to do this is to disallow pushing code that does not follows conventions, and checking for code style in the continuous integration pipeline.

Ruby on Rails developers are fond of their use of [Rubocop](https://github.com/rubocop-hq/rubocop) and share their rubocop configuration files with the community.

## Conclusion

One of the things that make a good software engineer *good* is their ability to adapt to work with different teams.
