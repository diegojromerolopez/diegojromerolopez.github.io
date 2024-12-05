---
title: The runtime type-checking operator in TypeScript
date: "2024-12-05T00:16:53+02:00"
draft: false
tags: ["software", "typescript", "ideas"]
---

# The runtime type-checking operator in TypeScript
I have been working with [TypeScript](https://www.typescriptlang.org/)
for a while but for sure I am not an expert in the language
(I feel more comfortable with Python).

I like the idea of type-safe but limiting the static type checking process
can make you confident about what you are getting from _outside sources_,
and if you do not trust those sources (you should NOT), you would need to include
a lot of repetitive checks any time we read data from the outside.

**This post is an intellectual exercise on how would I like TypeScript to be extended with runtime capabilities.**

## TypeScript types
TypeScript is a superset of Javascript created by Microsoft with the intent
of adding static typing to Javascript. Typescript code would be converted to
Javascript by a translation process (_transpiling_) that would be
hidden to the developer.

This language brings type checking to Javascript, but only statically. The types
are not checked at runtime, only when the

## The frontier problem
I am sure this issue has been treated before but with other name, but I like the idea
of getting some data from outside sources and dealing in our TypeScript code as a
_frontier_ between our project and outside world.

Having said that, the main issue I see with TypeScript is that the contract that we define
is not enforced unless we implement that check at runtime. Of course, you could argue that
that is not the scope of the language, but would that defeat the purpose of typing?

Let's see a fictitious example:

Suppose that we have been working in a task manager, and we have the Task type

```typescript
type Priority = "low" | "medium" | "high"

type Task = {
  id: string;
  title: string;
  description: string;
  completionDate?: Date;
  deadline?: Date;
  priority: Priority;
};
```

and we read the pending tasks from an external web service:

```typescript

const url = "https://example.com/api/tasks?status=pending"
const response = await fetch(url, {
  method: 'GET',
  headers: {"Content-Type": "application/json"},
});

if (!response.ok) {
  throw new Error(`HTTP error! status: ${response.status}`);
}

const { tasks }: { tasks: Task[] } = await response.json();
```

From the point of assignment of the constant tasks, it is assume that tasks is an array
of objects of type Tasks. Of course that does not need to be true, so we would need to check
the type in runtime.

```typescript
// This function would be defined elsewhere
function checkTasks(tasks: any): boolean {
  return Array.isArray(tasks) && tasks.every(taskI =>
    typeof taskI.id === 'string' &&
    typeof taskI.title === 'string' &&
    typeof taskI.description === 'string' &&
    taskI.completionDate !== undefined && typeof taskI.completionDate === 'Date' &&
    taskI.priority !== undefined && typeof taskI.deadline === 'Date' &&
    ["low",  "medium", "high"].includes(taskI.priority)
  );
}

checkTasks(tasks);
```

Or rely on an external library like
[zod](https://github.com/colinhacks/zod) to do that:

```typescript
import { z } from "zod";

const TaskSchema = z.object({
  id: z.string(),
  title: z.string(),
  description: z.string(),
  completionDate: z.string().datetime().optional(),
  deadline: z.string().datetime().optional(),
  priority: z.enum(["low", "medium", "high"])
});

function checkTasks(tasks: any): boolean {
  return Array.isArray(tasks) && tasks.every(taskI =>
    tasks.every(TaskSchema.safeParse().success;
  );
}
```

But... wouldn't be nice to have a built-in system in the language to do that?

## Proposal: runtime check operator

I would like TypeScript to be augmented with runtime capabilities that would grant it the
ability to check types.

A possible solution would be to have some validation library in the standard library (easy),
but as the enforcement of the type contract at runtime is one of the limitations of the
language, I would like to add an operator just for that.

Instead of doing:

```typescript
const { tasks }: { tasks: Task[] } = await response.json();
```

We could do:

```typescript
const { tasks }: { tasks: Task[] } <- await response.json();
```

The slim arrow operation, i.e. `<-`, would contain a runtime type check, and will raise
and exception when the type does not match the left variable in the assignment.

From that line onwards we could ensure the types as truthful.

You could argue that runtime type checks is outside the scope of TypeScript, but as it is
a common and frequent task, should not the language could be extended in that way? Do we need
to be limited to static checks only?

## Conclusion
We have _fantasized_ about adding a new operation to the types in TypeScript that would check
the type of a variable at runtime. We will delve with the implementation in next posts.
