---
title: "SOLUTION Exercise 3b: Set enviromental variables"
layout: page
---

*(You can download the files for this exercise, this contains the solution to the first part of this exercise: [ex3b.zip]({{ "/ex3b.zip" | relative_url }}).)*

## Part 1

Add this line to your Dockerfile:

```Dockerfile
ENV NAME=World
```

Then build the image, and run the container.

Now the server will produce "Hello World".

## Part 2

Run the container with the -e flag, like this:

```terminal
$ docker run -p 8000:8000 -e NAME=Me app:3b
```

Now the server will produce "Hello Me".



