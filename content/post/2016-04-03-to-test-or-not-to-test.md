---
title: To test or not to test
date: "2016-04-03T00:00:00+00:00"
draft: false
tags: ["software engineering", "tests"]
---

# Introduction

Some years ago I did not use any tests. We were cowboys in CodeWest where only fearful and strong people survive.

Sometimes we tested some actions and assumed that everything else worked fine. But for the most part, code where developed almost like our sub-conscience dictated us what to type: we were guided by instinct.

Of course, users of my applications were not so amused by this when they found software faulted and had to wait to me to repair it.

# Refactoring

In my last post I wrote about refactoring. This process allows us to improve software quality iteratively. That is, we should be always be refactoring our code, treating it like an evolving species.

# Tests

Every basic functionality must be tested by a test. That is the only way of knowing that our refactoring doesn't break our working software.

There are two kinds of tests: unit tests or functional tests. While unit tests assure me that core parts of software work fine, functional tests assert that what see the user is correct.

Testing with both types is a time-consuming task, but it is worth testing critical parts of software with unit and functional tests to assure the important parts work right.

# But what about changes in functionality?

One of the reasons we did not develop tests was because we believed it slowed down the agile process.

If you do tests, your throughput is lower, product owner validates functionality in a slower pace and the project can be slowed down or even stalled[^1].

My personal approach is:

- Product owner/Client wants some new feature.
- Show the client a storyboard that contains that functionality.
- Design succinctly the functionality.
- Code functionality as a prototype (without tests).
- Show the result to the client.
- If the result is approved:
- Test it to assure functionality remains during refactoring.
- Refactor it applying the best software design possible.
- If the result is rejected, throw it away.
- I suggest you to take a look to Test Driven Development even you don't apply it as is (as in my case[^2]).

Key concept here is prototyping. Many times, our client doesn't know that he/she wants. It could be because its business is not 100% specified or maybe his/her ideas of what he/she wants are not as clear as they should be. This way we deliver a working prototype that helps as an artifact to confirm or reject our idea of what the client wants[^3].

# Conclusion

Tests help us to assure that some functionality always works the desired way.

Refactoring and tests are two faces of the same coin. We cannot do one without the other.

Don't test functionality that is not validated by the client.

[^1]: Maybe software projects stalling is not a direct cause of a slow development but your client running out of money. Thus, client will be demotivated if no prototype is delivered early. In my experience, there can be no more than 1-2 weeks without deliveries (excluding first spike that defines project basis).

[^2]: There is some Test Driven Development criticism (e.g.: stackoverflow thread that argues that by using this technique, developers only intent is passing the test and not making a good software design. I partially agrees with that sentiment and that's the reason I wrote this post.

[^3]: A mockup storyboard is a good way to extract requirements but, in my experience, sometimes is not enough: business and external changes can make it obsolete once the working prototype is delivered.