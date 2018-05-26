---
title: "Exercise 3b: Set enviromental variables"
layout: page
---


Copy your directory from the previous exercise to a new directory called `ex3b`

```terminal
$ cp -r ex3a ex3b
$ cd ex3b
```

*You're on your own now ...*

## Part 1

Figure out how to modify your `Dockerfile` so that the `NAME` enviroment variable is set to "World". (Hint: read the documentation for the ENV statement in the [Dockerfile reference](https://docs.docker.com/engine/reference/builder/).)

Once you've modified your `Dockerfile`, rebuild the image, and run the container.

```terminal
$ docker build -t app:3b .
…
$ docker run -p 8000:8000 app:3b
```

## Part 2

Figure out how to set the `NAME` environment variable in the container at runtime. (Hint: read the documentation for the --env (-e) flag in the [docker run reference](https://docs.docker.com/engine/reference/commandline/run/).)

[\_]({{ "/ex3b-env-var-solution/" | relative_url }})
