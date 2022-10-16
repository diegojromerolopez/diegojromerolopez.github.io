---
title: Literate programming
date: "2015-08-25T00:00:00+00:00"
draft: false
tags: ["software engineering", "papers", "programming", "documentation"]
---

Donald E. Knuth coined the term Literate programming in this [paper](http://www.literateprogramming.com/knuthweb.pdf) he wrote almost 40 years ago.

Knuth wrote a tool called WEB as a demonstration of what Literate Programming should be. This tool would understand Pascal and TeX code, using Pascal code to create a binary executable and using TeX code to compile its documentation file. Pascal code would be a bit different because of the use of predefined macros and it would be interleaved by TeX code describing what actions execute.

WEB was composed by a weaver and a tangler. Its first component (the weaver) was code generator the would pick up the code, expand the macros and compile it, erase the texts of the resulting code and compile it. Its second component was an extractor of documentation written in TeX, where each block of code would be joined in one document that compiled the documentation of the program.

This amazing idea has been lost thru time. Sure, there are some self-documenting tools like Doxygen but there is no language that encourages documentation as a part of the programming task. Donald E. Knuth was ahead of his time (although he says there had been others before him) because of the foundational idea of his work: code must be able to be read like a literary piece.

This is what I encourage to my peers each day: code must be pleasant. Yes, it could be a bit strange reading "pleasure" and "code" but I would love to see a code with comments that really puts me in context, give me advice on how to use it, its order of algorithm complexity and inform me of whatever non-standard behavior I should know.

Nowadays we, software engineers, are not only worried by code that 'just works' but we are worried by making this code secure and easy to maintain and expand.

In my experience, when dealing with legacy code no documentation is given, only the code and this creates anxiety to the engineer and of course, to the stakeholders. Imagine if your company would have to base its business in a system that nobody knows. Not only its behavior but how it is done. But unfortunately, that is what usually happens.

I foresee a future language (or maybe an extension to an existing one) not specially worried in efficiency but in easy maintenance. This language could force programmers to write documentation for each sentence/block of code in a language similar to Simple English. Maybe this documentations could be styled in a simply markup language like Markdown.

Combine this with giving variable, function and class names a semantic meaning (based on common patterns?) and it will be the future bad-programmer-proof language.



