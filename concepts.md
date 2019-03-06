---
title: Docker Concepts
layout: page
---

"A virtual machine (VM) runs a full-blown 'guest' operating system with virtual access to host resources through a hypervisor. In general, VMs provide an environment with more resources than most applications need" (*[Get Started with Docker](https://docs.docker.com/get-started/#containers-and-virtual-machines)*).

![VM architecture](https://docs.docker.com/images/VM%402x.png)

"A container runs natively on Linux and shares the kernel of the host machine with other containers. It runs a discrete process, taking no more memory than any other executable, making it lightweight" (*[Get Started with Docker](https://docs.docker.com/get-started/#containers-and-virtual-machines)*).

![Container architecture](https://docs.docker.com/images/Container%402x.png)

"Docker uses a client-server architecture. The Docker client talks to the Docker daemon, which does the heavy lifting of building, running, and distributing your Docker containers. The Docker client and daemon can run on the same system, or you can connect a Docker client to a remote Docker daemon. The Docker client and daemon communicate using a REST API, over UNIX sockets or a network interface" (*[Docker overview](https://docs.docker.com/engine/docker-overview/#docker-architecture)*).

![Docker architecture](https://docs.docker.com/engine/images/architecture.svg)


"To many the light bulb moment comes when they realize that Docker is not a virtualization technology, it’s an application delivery technology" (*[Ebook: Docker for the Virtualization Admin](https://goto.docker.com/docker-for-the-virtualization-admin.html)*).

## Resources
- [Docker Cheat sheet (official)](https://www.docker.com/sites/default/files/Docker_CheatSheet_08.09.2016_0.pdf)
- [Docker Cheat sheet (community)](https://github.com/wsargent/docker-cheat-sheet)
