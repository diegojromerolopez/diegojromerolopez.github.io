---
title: How to write a simple middleware in deno fresh
date: "2024-12-26T00:00:00+02:00"
draft: false
tags: ["deno", "fresh"]
---

# How to write a simple middleware in deno fresh
Middlewares are layers that inject data or check the HTTP request and are used by a set of routes.
They are very useful as they group functionality together. Let's see how to implement a middleware
in deno fresh.

## Select the routes the middleware is going to affect
The middlewares in deno fresh are created inside a `_middleware.ts` file. This file will affect
the routes that are from its level to the bottom. Let's see an example:

Suppose we have this basic routes structure:

```sh
routes/
  - api/
    - task.ts
    - tasks.ts
    - user.ts
    - users.ts
  - index.ts
  - about.ts
```

To add a middleware that affect only the API, we will need to add it inside the api folder:

```sh
routes/
  - api/
    - _middleware.ts
    - task.ts
    - tasks.ts
    - user.ts
    - users.ts
  - index.ts
  - about.ts
```

If we were to add it in the routes folder, it will affect to the index and about routes, and all the API ones.

## Middleware structure

### Reader middleware

Let's suppose the API is authenticated by a token:

```typescript
// Suppose we have an import map in the deno.json
import { FreshContext } from "$fresh/server.ts";

export async function handler(req: Request, ctx: FreshContext<null>,) {
  // For simplicity we have hardcoded the secret token, DO NOT DO THIS!
  // Load it from a key or password secure server.
  const requestToken = req.headers.get("my-app-token")
  if(requestToken !== "SECRET TOKEN"){
    return Response.json({ status: "error", message: "Forbidden" }, status: 403);
  }

  // The next call will call to the next middleware or the route itself
  return await ctx.next();
}
```

The code is pretty straightforward, as we just read a request header and in the case
of an issue

### Injector middleware

```typescript
// Suppose we have an import map in the deno.json
import { FreshContext } from "$fresh/server.ts";

// Let's suppose that we want to create an unique request id (aka correlation id)
// and pass it down to all the routes.
type StateRequest = {
  requestId: string;
}

export async function handler(req: Request, ctx: FreshContext<StateRequest>,) {
  // Injection of unique id per request
  ctx.state.requestId = crypto.randomUUID();

  // The next call will call to the next middleware or the route itself
  return await ctx.next();
}
```

So when the route runs, it will be able to access to the request id:

```typescript
import { StateRequest } from "./_middleware.ts";

export const Handler: Handler<Context, StateRequest> = {
  async GET(req, ctx){
    const requestId = ctx.requestId;

    console.log(`The request id is ${requestId}`);

   return new Response.json({ uuid: requestId });
  }
}
```

### Conclusion
We have shown how to write two simple types of middlewares for the deno fresh
web framework: one that reads from the request, one that adds state to the
context.