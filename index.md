---
title: Docker Training
layout: page
---

# Setup

Install a Docker instance:

- [Docker for Mac](https://store.docker.com/editions/community/docker-ce-desktop-mac)
- [Docker for Windows](https://store.docker.com/editions/community/docker-ce-desktop-windows)

# Conceptual overview of Docker

"A virtual machine (VM) runs a full-blown 'guest' operating system with virtual access to host resources through a hypervisor. In general, VMs provide an environment with more resources than most applications need" (*[Get Started with Docker](https://docs.docker.com/get-started/#containers-and-virtual-machines)*).

![VM architecture](https://www.docker.com/sites/default/files/VM%402x.png)

"A container runs natively on Linux and shares the kernel of the host machine with other containers. It runs a discrete process, taking no more memory than any other executable, making it lightweight" (*[Get Started with Docker](https://docs.docker.com/get-started/#containers-and-virtual-machines)*).

![Container architecture](https://www.docker.com/sites/default/files/Container%402x.png)

"Docker uses a client-server architecture. The Docker client talks to the Docker daemon, which does the heavy lifting of building, running, and distributing your Docker containers. The Docker client and daemon can run on the same system, or you can connect a Docker client to a remote Docker daemon. The Docker client and daemon communicate using a REST API, over UNIX sockets or a network interface" (*[Docker overview](https://docs.docker.com/engine/docker-overview/#docker-architecture)*)

![Docker architecture](https://docs.docker.com/engine/images/architecture.svg)


-  [Exercise 1:]({{ "/ex1-run-an-ubuntu-container/" | relative_url }})
-  [Exercise 2:]({{ "/ex2-home-directory-webserver/" | relative_url }})
-  [Exercise 3: Add Redis]({{ "/ex3-add-redis/" | relative_url }})
