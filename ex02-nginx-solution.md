---
title: "SOLUTION Exercise 2: Home directory web server"
layout: page
---

Change to the `ex02` directory, and use this Docker `run` command

```terminal
$ docker run -v $(pwd)/ex02:/usr/share/nginx/html:ro -p 8080:80 nginx
Unable to find image 'nginx:latest' locally
latest: Pulling from library/nginx
f2aa67a397c4: Pull complete
3c091c23e29d: Pull complete
4a99993b8636: Pull complete
Digest: sha256:0fb320e2a1b1620b4905facb3447e3d84ad36da0b2c8aa8fe3a5a81d1187b884
Status: Downloaded newer image for nginx:latest
```

This will start a new container based on the `nginx` image. It will pull the image first if it doesn't already exist locally.

You can connect to the server in your browser at http://127.0.0.1:8080/ (or use `curl http://127.0.0.1:8080/` if you're running Docker somewhere else).

Use ^C to stop the server.
