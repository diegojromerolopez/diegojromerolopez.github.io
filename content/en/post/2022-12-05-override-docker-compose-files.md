---
title: Override docker-compose.yml files
date: "2022-12-05T19:50:00+01:00"
draft: false
tags: ["docker", "docker-compose"]
---

# Override docker-compose.yml files

Sometimes we want to have different versions of docker-compose.yml files
(one for production and one for development). Each environment has their
own characteristics (slightly different images for example) we show here
a good way to override sections of a docker-compose.yml file easily.

## Why?
Sometimes we have several environments that share almost all docker configuration.
Having a common docker-compose.yml file and several docker-compose.override.yml
files is a great way to manage your service configurations.

## How?
[Use several docker-compose.yml files](https://docs.docker.com/compose/extends/#multiple-compose-files).

You only have to create several docker-compose.yml files
and [replicate the section of the service you want to add, overwrite or extend](https://docs.docker.com/compose/extends/#adding-and-overriding-configuration).

Let us see an example:

```yml
# docker-compose.yml
version: "3.9"

services:
  db:
    hostname: project_db
    container_name: project_db
    image: postgres
    environment:
      - POSTGRES_DB=project
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
    ports:
      - '5432:5432'
    restart: always
    volumes:
      - db:/var/lib/postgresql/data
    networks:
      - project_network

  rabbitmq:
    hostname: project_rabbitmq
    container_name: project_rabbitmq
    image: rabbitmq:3-management-alpine
    ports:
      - 5672:5672
      - 15672:15672
    environment:
      - RABBITMQ_USER=guest
      - RABBITMQ_PASSWORD=guest
    volumes:
      - ./tmp/rabbitmq/data/:/var/lib/rabbitmq/
      - ./tmp/rabbitmq/log/:/var/log/rabbitmq
    networks:
      - project_network
    healthcheck:
      test: [ "CMD", "curl", "-f", "http://localhost:15672" ]
      interval: 30s
      timeout: 10s
      retries: 5

  web:
    hostname: project_web
    container_name: project_web
    build:
      context: .
      dockerfile: ./docker/web/Dockerfile
    command: /opt/app/docker-entrypoint.sh
    ports:
      - "9000:9000"
    environment:
      - DB_BACKEND=postgresql
      - DB_NAME=project
      - DB_USER=postgres
      - DB_PASSWORD=postgres
      - DB_HOST=project_db
      - DB_PORT=5432
      - QUEUE_HOST=project_rabbitmq
      - QUEUE_PORT=5672
      - LOG_NAME=web
      - LOG_LEVEL=INFO
    depends_on:
      - db
      - rabbitmq
    networks:
      - project_network
    restart: always

networks:
  project_network:
    name: project_network
    driver: bridge
volumes:
  db:
    driver: local
  project_rabbitmq:
    driver: local
```

Imagine we want to use a different Dockerfile for the project's *web* service tests.
You only need to create a different docker-compose.yml (with a meaningful name
like **docker-compose.web-test-override.ymll**) and overwrite the property dockerfile
of the main docker-compose.yml file.

```yml
# docker-compose.web-test-override.yml
version: "3.9"

services:
 web:
    build:
      dockerfile: ./docker/web/web.Dockerfile
    environment:
      - LOG_LEVEL=DEBUG
```

In our case, we have override the property dockerfile and the LOG_LEVEL environment variable.

## How do you use it?

Use the **-f** or **--file** parameter to add several files to the docker-compose
command you want to use, e.g.

```sh
docker-compose -f docker-compose.yml -f docker-compose.web-test.override.yml run web
```

## What's the *catch*?
You only can overwrite sections that containe a lone value. In the case of
sections with several values (like ports), you can add new values but not
remove or overwrite entirely the section.

So maybe a good practice is to have multiple-value sections in different
docker-compose.yml files.

# Conclusion
You can use several docker-compose.yml with the intent of overwritting
concrete parts of a main docker-compose.yml file. This can be useful
for customizing properties and sharing most of the configuration for
different environments.
