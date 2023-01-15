---
title: Use the builder stage pattern in Dockerfiles
date: "2023-01-15T00:00:00+01:00"
draft: true
tags: ["docker"]
---

# Use the builder stage pattern in Dockerfiles
Most of the time, some libraries that we install in a
docker image are only used for the construction of our
executables. Could we just not include in our final docker image?

## Docker images should be minimal
As we saw in our
[previous post](/blog/2023/01/reduce-the-size-of-your-docker-images),
docker images should be minimal for several reasons, but the
aim is to reduce the cost of the transference of the docker image.

## The builder pattern
By having a stage build the required files, we can create a slimmer
docker image by using
[multi-stage builds](https://docs.docker.com/build/building/multi-stage/).
We can see a golang example that follows this pattern:

```dockerfile
# TODO: review this Dockerfile before publication
FROM golang:latest as builder
WORKDIR /app
COPY go.mod ./
COPY go.sum ./
RUN go mod download
COPY . .
RUN go build -o main

FROM alpine:latest as release
RUN apk --no-cache add ca-certificates
WORKDIR /app
COPY --from=builder /app/main ./
CMD ["./app"]
```

The difference with respect to the traditional approach is that
only the binary is copied to the release image, so the final
image is going to be smaller (without all the golang modules).

## The builder pattern in interpreted languages
You could think that this pattern can only be used for compiled languages
(like golang), but what about interpreted languages? Is there any way
to reduce the size of docker images using this pattern?

```dockerfile
FROM ruby:2.5.5-alpine AS builder
ENV WORKDIR /app
ENV BUNDLE_PATH="/app/bundle"
# Add the required packages for your ruby application
RUN apk add --update build-base
COPY . $WORKDIR
RUN bundle install

FROM ruby:2.5.5-alpine AS dev
ENV BUNDLE_PATH="/app/bundle"
COPY --from=builder $BUNDLE_PATH $BUNDLE_PATH
```

## Conclusion
Garden your Dockerfile and use the builder pattern to
keep their size small.
