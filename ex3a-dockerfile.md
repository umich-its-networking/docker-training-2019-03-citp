---
title: Create an application and Dockerfile
layout: page
---

*(You can download the files for this exercise: [ex3a.zip]({{ "/ex3a.zip" | relative_url }}), and skip the file creation steps.)*

Create a new directory called `ex3a`

```terminal
$ mkdir ex3a
$ cd ex3a
```

In the new directory, create a file called `Dockerfile` with these contents:

```dockerfile
FROM python:3.6-slim

ENV FLASK_DEBUG=1

COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt

WORKDIR /usr/src/app
ADD . /usr/src/app

EXPOSE 8000

CMD ["python", "app.py"]
```

Create a file called `requirements.txt` with these contents:

```
Flask==1.0.2
```

Create a file called `app.py` with these contents:

```python
from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def root():
    return 'Hello %s' % os.getenv('NAME')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
```

Build the image with the `build` command. If you don't have the `python:3.6-slim` image, Docker will fetch it for you because our Dockerfile is based on it.

```terminal
$ docker build -t app:3a .
Sending build context to Docker daemon   16.9kB
Step 1/8 : FROM python:slim
slim: Pulling from library/python
4d0d76e05f3c: Pull complete
5d78e1900166: Pull complete
7b6e0da887f5: Pull complete
8592f81e0e83: Pull complete
ce808ea78164: Pull complete
Digest: sha256:9ac457a996755a468b414c0889d10edfb1ff1589eaf4c5e2cf701a88f26ee9fc
Status: Downloaded newer image for python:slim
 ---﹥ d6f22b3a2b87
Step 2/8 : COPY requirements.txt /tmp
 ---﹥ eccbe3c1840d
Step 3/8 : RUN pip install -r /tmp/requirements.txt
 ---﹥ Running in d844cd51363e
Collecting flask (from -r /tmp/requirements.txt (line 1))
  Downloading https://files.pythonhosted.org/packages/7f/e7/08578774ed4536d3242b14dacb4696386634607af824ea997202cd0edb4b/Flask-1.0.2-py2.py3-none-any.whl (91kB)
Collecting click﹥=5.1 (from flask-﹥-r /tmp/requirements.txt (line 1))
  Downloading https://files.pythonhosted.org/packages/34/c1/8806f99713ddb993c5366c362b2f908f18269f8d792aff1abfd700775a77/click-6.7-py2.py3-none-any.whl (71kB)
Collecting Jinja2﹥=2.10 (from flask-﹥-r /tmp/requirements.txt (line 1))
  Downloading https://files.pythonhosted.org/packages/7f/ff/ae64bacdfc95f27a016a7bed8e8686763ba4d277a78ca76f32659220a731/Jinja2-2.10-py2.py3-none-any.whl (126kB)
Collecting itsdangerous﹥=0.24 (from flask-﹥-r /tmp/requirements.txt (line 1))
  Downloading https://files.pythonhosted.org/packages/dc/b4/a60bcdba945c00f6d608d8975131ab3f25b22f2bcfe1dab221165194b2d4/itsdangerous-0.24.tar.gz (46kB)
Collecting Werkzeug﹥=0.14 (from flask-﹥-r /tmp/requirements.txt (line 1))
  Downloading https://files.pythonhosted.org/packages/20/c4/12e3e56473e52375aa29c4764e70d1b8f3efa6682bef8d0aae04fe335243/Werkzeug-0.14.1-py2.py3-none-any.whl (322kB)
Collecting MarkupSafe﹥=0.23 (from Jinja2﹥=2.10-﹥flask-﹥-r /tmp/requirements.txt (line 1))
  Downloading https://files.pythonhosted.org/packages/4d/de/32d741db316d8fdb7680822dd37001ef7a448255de9699ab4bfcbdf4172b/MarkupSafe-1.0.tar.gz
Building wheels for collected packages: itsdangerous, MarkupSafe
  Running setup.py bdist_wheel for itsdangerous: started
  Running setup.py bdist_wheel for itsdangerous: finished with status 'done'
  Stored in directory: /root/.cache/pip/wheels/2c/4a/61/5599631c1554768c6290b08c02c72d7317910374ca602ff1e5
  Running setup.py bdist_wheel for MarkupSafe: started
  Running setup.py bdist_wheel for MarkupSafe: finished with status 'done'
  Stored in directory: /root/.cache/pip/wheels/33/56/20/ebe49a5c612fffe1c5a632146b16596f9e64676768661e4e46
Successfully built itsdangerous MarkupSafe
Installing collected packages: click, MarkupSafe, Jinja2, itsdangerous, Werkzeug, flask
Successfully installed Jinja2-2.10 MarkupSafe-1.0 Werkzeug-0.14.1 click-6.7 flask-1.0.2 itsdangerous-0.24
Removing intermediate container d844cd51363e
 ---﹥ 665b12a89ea9
Step 4/8 : WORKDIR /usr/src/app
Removing intermediate container 59e6c59d4ffa
 ---﹥ d7534b760c58
Step 5/8 : ADD . /usr/src/app
 ---﹥ 8ff522120db8
Step 6/8 : EXPOSE 8000
 ---﹥ Running in fe347f54df39
Removing intermediate container fe347f54df39
 ---﹥ 0ac393abc69d
Step 7/8 : ENV FLASK_DEBUG 1
 ---﹥ Running in 0a760c430221
Removing intermediate container 0a760c430221
 ---﹥ 73b59be52911
Step 8/8 : CMD ["python", "app.py"]
 ---﹥ Running in e7b9e2c84b9b
Removing intermediate container e7b9e2c84b9b
 ---﹥ 769f7e92e6bf
Successfully built 769f7e92e6bf
Successfully tagged ex3a:latest
```

Try running the same command again. Note that the output is different, and that it runs much faster, because the work has already been done and Docker is taking advantage of its cache.

```terminal
$ docker build -t app:3a .
Sending build context to Docker daemon  4.096kB
Step 1/8 : FROM python:slim
 ---﹥ d6f22b3a2b87
Step 2/8 : COPY requirements.txt /tmp
 ---﹥ Using cache
 ---﹥ eccbe3c1840d
Step 3/8 : RUN pip install -r /tmp/requirements.txt
 ---﹥ Using cache
 ---﹥ 665b12a89ea9
Step 4/8 : WORKDIR /usr/src/app
 ---﹥ Using cache
 ---﹥ d7534b760c58
Step 5/8 : ADD . /usr/src/app
 ---﹥ 5a5204bf3ee7
Step 6/8 : EXPOSE 8000
 ---﹥ Running in 2290ef65657b
Removing intermediate container 2290ef65657b
 ---﹥ b914a181c014
Step 7/8 : ENV FLASK_DEBUG 1
 ---﹥ Running in d9daa4323887
Removing intermediate container d9daa4323887
 ---﹥ 76741c8ce75c
Step 8/8 : CMD ["python", "app.py"]
 ---﹥ Running in 25c39491e29d
Removing intermediate container 25c39491e29d
 ---﹥ e0f91cc3e501
Successfully built e0f91cc3e501
Successfully tagged ex3a:latest
```

Run a container based on the `ex3a` image.

```terminal
$ docker run -p 8000:8000 app:3a
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:8000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 146-234-553
```

You can connect to the server by going to http://127.0.0.1:8000/ in your browser (or by using `curl http://127.0.0.1:8000/`).

The output will say "Hello None". This is because the app.py code is looking for a value in the enviroment, and since it doesn't find it, it defaults to "None". We'll fix this in the next exercise.
