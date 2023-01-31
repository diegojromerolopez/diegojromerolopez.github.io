---
title: Reduce the size of your builder images
date: "2023-01-14T00:00:00+01:00"
draft: false
tags: ["docker"]
---

# Reduce the size of your builder images
Docker images should have a small size. For example, Alpine Linux images
have a mere 50MB of size, debian-slim is 50-60MB of size.
Why do we seek a small size footprint? One reason is simply because the
docker images are usually pushed to, and download from, docker repositories like
[dockerhub](https://hub.docker.com/) or other private docker repositories.

## Use a small base image
Alpine and debian-slim-stable are like 50MB. Use these kind of
images instead of bigger images.

## Copy only the required files
Use **COPY** with care, and always make use of a .dockerignore to avoid
copying folders and files that the image does not need but that
*are heavy* in regards of space.

Instead of doing
```dockerfile
COPY . .
```
Copy individual files and folders

```dockerfile
COPY src/ .
```

A common dockerignore for a python project could be the following:
```
.git
build
coverage
tmp
venv
.idea
.vscode
```

## Reduce the number of docker layers
Each docker layer occupies a certain amount of space, by reducing them
you can achieve some reduction of the size of the docker image.

Instead of:

```dockerfile
RUN apt update
RUN apt upgrade
RUN apt install -y curl
```
Do:

```dockerfile
RUN apt update && \
    apt upgrade && \
    apt install -y curl
```

## Remove caches, logs and temporal information
Try to remove all information that is not

```dockerfile
# Install a package, don't install more packages than the required ones
# and clean the apt cache and remove orphaned packages.
RUN apt update && \
    apt upgrade && \
    apt install -y --no-install-recomends curl && \
    apt clean && \
    apt autoremove
```

## Conclusion
There are other ways to reduce the size of docker images,
like using [dive](https://github.com/wagoodman/dive) to check
the size of each docker layer, and of course the use of the
builder pattern, that we will shown in the future.

However, this post has shown some
basic advice to reduce the size of docker images, and that
was my intent here.
