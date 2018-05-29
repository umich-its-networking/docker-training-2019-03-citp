---
title: "SOLUTION Exercise 5: Add Redis"
layout: page
---

## Part 1

Before we can link a Redis container to our app, it needs to be running.

```terminal
$ docker run --name my-redis --detach redis
Unable to find image 'redis:latest' locally
latest: Pulling from library/redis
4d0d76e05f3c: Pull complete
cfbf30a55ec9: Pull complete
82648e31640d: Pull complete
fb7ace35d550: Pull complete
497bf119bebf: Pull complete
89340f6074da: Pull complete
Digest: sha256:4aed8ea5a5fc4cf05c8d5341b4ae4a4f7c0f9301082a74f6f9a5f321140e0cd3
Status: Downloaded newer image for redis:latest
53581318b180195595fc5f4b58b40f5dc6987a13726be6e1df1af1884f5161fe
```

A couple of things to note:
  - the `--detach` flag runs the container in the background
  - the `--name` flag makes this container easier to reference in the next command

## Part 2

Now we can link the `my-redis` container to our app when we run its container.

```terminal
$ docker run -p 8000:8000 --link my-redis app:05
```

Now when you connect to the app in your browser, you should be able to add entries to the guest book.

