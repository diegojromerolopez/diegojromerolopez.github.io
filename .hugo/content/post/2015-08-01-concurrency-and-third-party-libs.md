---
title: Concurrency and third party libraries
date: "2015-08-01T00:00:00+00:00"
draft: false
tags: ["software engineering", "python"]
---

Last friday, one of my mates had a strange error in his code: incoherent an irrepetible results arise en each execution.

His code (Python) was concurrent code and each thread used several libraries (BeautifulSoup4[^1] was one of them) which they were not thread-safe. What does it mean? It means we cannot assure that atomicity is achieved in some operations executed by the threads, effectively sharing some data that must not be shared.

I ended up helping him to set a critical section in these not-thread-safe parts of his code but this situation kept me wondering why a library that parses XML is not thread-safe and what kind of common resources used of the system. I couldn’t spend more time investigating this issue but this kept me wondering if this “feature” is not a case of bad software design.

Take a look if everything you are using is thread-safe before you start partitioning your execution flow in threads.

[^1]: Technically, BeautifulSoup4 is a wrapper, not a library. Developer can choose several parsers available (html5lib, lxml…) when using it in an application. Html5lib library is what we were using at the time. ↩