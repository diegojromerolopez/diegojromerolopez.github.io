---
title: How to manage docker secrets
date: "2023-08-12T00:00:00+02:00"
draft: false
tags: ["docker", "secrets", "security"]
---

# How to manage docker secrets
The product that is produced by most software developer teams is a docker image.
How can be sure that we are not leaking secrets in docker images? If we include
them as building arguments for sure they are going to be stored in the own image.
Is there any way to avoid having them inside the docker image?

## Introduction
Suppose you have a docker image that requires a secret, you do not want to include
it in the image, but you need during the process of building the image. In other words,
you cannot pass the secrets as environment variables because you need during the
construction of the image, not when running a container based on that image.

A good way of checking what we have in each layer of the docker image is use the tool
[dive](https://github.com/wagoodman/dive).

Anyway, let us continue with Docker and secrets.

## Docker secrets
Docker support the use of [secrets](https://docs.docker.com/engine/swarm/secrets/), and
that is the easiest way of including secrets to your docker images.

First, you can use secrets while building docker images using the build command:

```sh
DOCKER_BUILDKIT=1 \
docker build --secret id=my_env_secret,env=MY_ENV_SECRET .
```

```sh
DOCKER_BUILDKIT=1 \
docker build --secret id=my_env_secret,src=my_secret_file .
```

Second, you can include secrets in your
[docker-compose.yml](https://docs.docker.com/compose/use-secrets/) file:

```yml
version: "3.8"

services:
  app:
    build: app:latest
    secrets:
      - my_file_secret
      - my_env_secret

secrets:
  my_file_secret:
    file: ./my_file_secret.txt
  my_env_secret:
    env: "MY_ENV_SECRET_VARIABLE"
```

As long as you have a my_file_secret.txt file with the secret and a MY_ENV_SECRET_VARIABLE
environment variable with the other secret, you only need to include the
secret in your Dockerfile file:

```Dockerfile
RUN --mount=type=secret,id=my_env_secret \
    MY_ENV_SECRET=$(cat /run/secrets/my_env_secret) <command that uses the my_env_secret>
```

Notice that it is the same with the *file* secret but replacing my_env_secret by my_file_secret.

Where `<command that uses the my_env_secret>` is just a command that uses the secret, for example, and installation of a private python package:

```Dockerfile
RUN --mount=type=secret,id=my_env_secret \
     pip install https://user:$(cat /run/secrets/my_env_secret)@artifactory.example.com/artifactory/team/package-1.1-py3-none-any.whl
```

The same can be done with the my_file_secret, but I am not going to lie to you. I prefer
to use environment secrets as it is easier to deal with environment variables than with
files.

Anyway, once you have it you are all set and can build the docker image:

```sh
docker compose build app
```

## Conclussion
Never passs secrets as build-args as they will be visible in the docker image layers.
That is less than ideal as the secrets stop being secrets. Use the secrets functionality
of docker to have actually secret variables.
