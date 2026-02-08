---
title: Release always, even partial features
date: "2026-02-08T00:00:00+02:00"
draft: false
tags: ["agile", "war-story"]
---

# Release always, even partial features
Have you wondered what to do when a feature takes more time than the scheduled one?
What can you do if you reach the deadline but the feature is incomplete?

## Introduction
In this post I will tell an early in my career story when
I first learned that the release of anything is always
better than release nothing.

## The contract
There was a contact where the company I worked for at that time, needed to provide a web service
to a local branch of one of the most important companies in the world of c...[^1].

Engineering was not in the meeting and was only informed after that that they
need to release a full product in 3 months.

We had been using this project for other minor clients, but we did not know if it could deal with
the load of work that this particular client required.

## Death March
[This term is coined by Edward Yourdon](https://en.wikipedia.org/wiki/Death_march_(project_management))
in his book Death March, meaning a project that needs significant overwork to be completed on the scheduled
time.

That is exactly what I was doing at the time: overworking myself.

## Agility
In the agile world usually the client is kept in the loop by the product owner, and they have
periodical updates about the development of the project. In case of a delay, the first thing
is to inform the client.

From the first moment I informed the scrum master that the deadline was not possible.
There was a total disconnection between management and the engineering department,
so it was expected. But I warned them that the project will not be 100% completed.

The response was surprising for me: *Do what you can and we will deal with the client*.

But for them, it was not surprising, they had long-term clients with a long-standing relationship,
so delays and iterative improvements were totally expected. This was just another project for them.

## MVP
I decided that I needed to cut corners and reduced the scope of the project. Not much, but
(and this is the important lesson) enough to give me time to have the critical functionality
up and running for the deadline.

The main idea is that you need to release a minimum working product where if not possible
to be on time, it lacks some non-critical parts.

I decided to unload some of the features to external providers, giving the option of using them
or using the in-house technology[^2]. The software dealt with websites, so each website had a
configuration that can be set to use a different solution, depending on the difficulty of the
problem (web scraping).

## Release!
The application was working fine and extracting the
information. We had some minor issues but all the issues were resolved (or mitigated).
I left the company just before the release, so I did not enjoy the satisfaction of a well done job
(although we kept in contact for a while and they remember my presence there fondly[^3]).

## Lessons learned
**Do not overwork**: overworking leads to burnout, and that worsens mental and physical health,
and of course, the relationships among members of the team.

**Release something**: even if you thing that it is not worth it. What scares the most to people
is not knowing the state of the project. Being updated regularly (more even so in case of delays)
is crucial for keeping the project alive and a good relationship with the client.

## Conclusion
I have described a situation where a feature could not be released directly,
but instead of blocking the full project, I decided to **iteratively release improvements**
of the project. First, a partial version of the feature. Then refinement of those until
the quality is good enough.

The aim of this process is double: keeping a good relationship with the client,
and getting early feedback of the new features.

[^1]: deliberate omission.

[^2]: without giving more information, let me say that the project dealt with scraping web pages and that problem has a lot of uncertainty. Being blocked or rate-limited, having to retry the requests, invalid HTTP responses,
dynamic frontend applications that need to be scraped via a headless browser, etc.

[^3]: even though I left the company before the release, I took no vacation that year to make sure the
process was fully smooth.
