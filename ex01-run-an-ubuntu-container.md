---
title: "Exercise 1: Run an Ubuntu container"
layout: page
---

The exercise will demonstrate the ephemerality of a Docker container.

Start by pulling the Ubuntu Docker image from Docker Hub.

```terminal
$ docker pull ubuntu
Using default tag: latest
latest: Pulling from library/ubuntu
a48c500ed24e: Pull complete
1e1de00ff7e1: Pull complete
0330ca45a200: Pull complete
471db38bcfbf: Pull complete
0b4aba487617: Pull complete
Digest: sha256:c8c275751219dadad8fa56b3ac41ca6cb22219ff117ca98fe82b42f24e1ba64e
Status: Downloaded newer image for ubuntu:latest
```

Create a Docker container based on the Ubuntu image with the `docker run` command.

```terminal
$ docker run -i -t ubuntu /bin/bash
root@44757783c537:/# 
```

Note that you now have a bash shell inside the container. That funny text after `root@` is the container's hostname in the Docker environment, so it will be different on your machine.

Create a file in the root of the filesystem in the container.

```terminal
root@44757783c537:/# ls /
bin   dev  home  lib64  mnt  proc  run   srv  tmp  var
boot  etc  lib   media  opt  root  sbin  sys  usr
root@44757783c537:/# touch /something
root@44757783c537:/# ls -l /something
-rw-r--r-- 1 root root 0 May 24 20:20 /something
```

Exit the container.

```terminal
root@44757783c537:/# exit
exit
$
```

Create a new container by running the same `docker run` command as before. Then try to list the `/something` file.

```terminal
$ docker run -i -t ubuntu /bin/bash
root@473d78109f8b:/# ls -l /something
ls: cannot access '/something': No such file or directory
```

Also note that the hostname is different. This is a different container.

While the ubuntu container is still running, open another terminal session and list the running processes in Docker.

```terminal
$ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
6501c99676fe        ubuntu              "bash"              9 seconds ago       Up 9 seconds                            frosty_payne
```
