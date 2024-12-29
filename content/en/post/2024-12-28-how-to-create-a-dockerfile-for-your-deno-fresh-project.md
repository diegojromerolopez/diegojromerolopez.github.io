---
title: How to create a Dockerfile for your deno fresh project
date: "2024-12-28T00:00:00+02:00"
draft: false
tags: ["deno", "fresh", "docker"]
---

# How to create a Dockerfile for your deno fresh project
Sometimes creating a Dockerfile is an art, you need to be aware of what files include in each layer to leverage
the docker cache. How can we do this with [deno fresh](https://fresh.deno.dev/)?

## Recommended or usual Dockerfile
Most of the examples I have found in the internet
([like this one](https://geshan.com.np/blog/2024/07/deno-docker/#step-3%3A-dockerize-deno-fresh))
tend to copy all the files in the same Docker instruction:

```Dockerfile
FROM denoland/deno:2.1.4

WORKDIR /app

COPY . .
RUN deno cache main.ts
RUN deno task build

USER deno
EXPOSE 8000

CMD ["run", "-A", "main.ts"]
```

This of course works, but we are just copying all the files in the Docker image,
and that can cause many issues:

1. Inclusion of files that are not needed.
2. Inclusion of dangerous files.

Of course you could argue that that is why we should we using a .dockerignore file,
however, we are not caching almost anything in the Dockerfile. We could it better,
although more verbose.

## My approach

```Dockerfile
FROM denoland/deno:2.1.4

WORKDIR /app

COPY deno.json deno.json
COPY dev.ts dev.ts

COPY fresh.config.ts fresh.config.ts
COPY fresh.gen.ts fresh.gen.ts

COPY tailwind.config.ts tailwind.config.ts

COPY main.ts main.ts

COPY components components
COPY islands islands
COPY static static

COPY lib lib
COPY tests tests

RUN deno cache main.ts
RUN deno task build

USER deno
EXPOSE 8000

CMD ["run", "-A", "main.ts"]
```

I know it looks longer, and more verbose, but I like explicit code. I do not want to deal with
copying the .git or tmp folder by mistake, and finding that the docker images is leaking
information that should not.

All folders and files but lib and tests are mandatory for deno fresh. Those are for my application
and test code (resp.). You can name them in the way you like.

As you see here, most of the time we will rely on the docker cache when building the image. Most
of the time the configuration files are not modified at all, and this approach would save us
some precious time.

## Conclusion
Having a explicit code (even in Dockerfiles) makes my life easier. Make sure you understand how the docker cache works when building a docker image, and leverage that power.