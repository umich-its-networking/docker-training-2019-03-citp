---
title: "SOLUTION Excercise 2: Home directory web server"
layout: page
---

From the `ex2` directory, run this one-liner:

```terminal
$ docker run -v $(pwd):/usr/share/nginx/html:ro -p 8080:80 nginx
```

This will start a new container based on the `nginx` image. It will pull the image first if it doesn't already exist locally.

You can connect to the server in your browser at http://127.0.0.1:8080/ (or the IP of the host where you're running Docker on).

Use ^C to stop the server.
