---
title: Allow writing of files in docker in Linux
date: "2022-10-17T18:49:00+02:00"
draft: false
tags: ["docker", "linux", "tips"]
bigimg: [{src: "/img/shipping-containers.jpeg", desc: "Public domain image from Pexels (https://www.pexels.com/photo/blue-white-orange-and-brown-container-van-163726/)"}]
---

Docker is a container system that allow developers to have a common
environment to develop and SRE/devops to have machine-independent
deployment process. 

# Allow writing of files in docker in Linux

I have been working on a small project in Python:
[functainer](https://github.com/diegojromerolopez/functainer).
The goal of this project is to provide a Python package to run functions
in docker seamlessly: you only will docker and Python to run it.

Anyway, that project uses files as a mean of communication, i.e.
there is a file volume that the container uses to write the
output, and make it reachable by the host.

When the host is a Linux machine, docker daemon runs on root user,
and that user is not the same than yours (obviously).
A way to avoid having a **Permission Denied error** is to run
your container with your user y making use of --user parameter
in the [docker container run command](https://docs.docker.com/engine/reference/commandline/container_run/), e.g.:

```bash
docker run -it --rm \
  --mount "type=bind,src=/tmp/shared,dst=/tmp/output" \
  --user "$(id -u):$(id -g)" \
  ubuntu:latest "echo \"whatever content readable by host\" > /tmp/output"
```

I got the idea of changing the user from
this [post by Vladislav Supalov](https://vsupalov.com/docker-shared-permissions/),
he has a [blog](https://vsupalov.com/) where he writes about interesting matters.

In functainer, you can see that that is exactly what I am doing
using the Python [Docker SDK for Python](https://docker-py.readthedocs.io/en/stable/index.html):

```python
docker_client.containers.run(
    image=image,
    command=f'{python_command} /tmp/dockerizer_temp/executor.py',
    volumes=[
        f'{temp_dir_path}:/tmp/dockerizer_temp',
        f'{output_file_path}:/tmp/dockerizer_output'
    ],
    remove=True,
    user=f'{os.getuid()}:{os.getgid()}',
    **run_container_kwargs
)
```

Of course, there are other possible solutions, like adding the user
to the docker group but... It makes me feel uneasy, as the user would
have some root privileges. Thus, I want functainer to run as-is, without
needing any system-wide change.

P.S. I will write a post about functainer soon!