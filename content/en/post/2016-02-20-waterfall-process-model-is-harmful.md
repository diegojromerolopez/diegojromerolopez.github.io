---
title: Waterfall process model is harmful
date: "2016-02-20T00:00:00+00:00"
draft: false
tags: ["software engineering", "education"]
---

# Introduction

Waterfall model is a development process based on doing software development processes one after another and not looking back.

Here is a simple diagram (from [Waterfall model article in Wikipedia](https://en.wikipedia.org/wiki/Waterfall_model)) of that model:

![/static/images/waterfall-model-from-wikipedia.png](/static/images/waterfall-model-from-wikipedia.png)

# Waterfall model

That is it supposes we are infallible and the client is infallible so each phase is perfect and serves well enough the next.

# Issues with waterfall model

Waterfall process model suffered a total criticism by Winston W. Royce in his paper Managing the development of large software systems, published in the Proceedings of IEE WESCON in August 1970.

In this paper, Royce clearly showed that he was fully against using this step-by-step process. Indeed, in the second page of this work he said: I believe in this concept, but the implementation described above is risky and invites failure.

Why he was so vehenmetly against the waterfall model? The rest of the paper gives some support to his claim being the most important these ones:

If some error is detected in test phase, there can be needed changes in requirement phase.
The program design phase can create changes in software requirement phase.
Already in 1970 there were voices that claimed waterfall model was not adequate for software engineering.

# Solutions for this flawed model

In his paper, Royce defined what he called an early simulation of the final product, where the process of developing early prototipos of software that can affected each one of the phases of the model. So, what we call iterations or early releases to the client was almost defined in 1970! Not in the '90s but 40 years before the agile manifesto.

The relase often adagio and the idea of releasing working software is also present in this paper: They must quickly sense the trouble spots in the design, model them, model their alternatives, forget the straightforward aspects of the design which aren't worth studying at this early point, and finally arrive at an error-free program.

Royce, furthermore, advocate for involving the client during the software development process: To give the contractor free rein between requirement definition and operation is inviting trouble.

# Why he was forgotten?

Well, this paper is hard to read because it has no clear aim. He is criticizing a software development model but also advocating fo a new one that is not very clear presented. His new model has some agile features but also mixes some of his heuristic solutions to problems he has experimented. Maybe too much detail in the description of his model is the cause people didn't put his teachings in practice. I had a hard time separating the basic principles from his particular model.

To make things worse it has many figures that, if you don't fully read it, can give you a misleading idea of what Royce is showing here.

In that time there were no software engineers, only programmers with different backgrounds. I can assume this paper mislead many people into thinking that this model was enough for their non-critical software developments.

Royce doesn't use the term "waterfall"[^1] along the paper so maybe he was ahead of his time and was not understood.

[^1]: "Waterfall" was coined in 1976 by Bell and Thayer.