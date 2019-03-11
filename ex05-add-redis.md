---
title: "Exercise 5: Add Redis"
layout: page
---

*(You can download the files for this exercise: [ex05.zip]({{ "/ex05.zip" | relative_url }}), and skip the file update steps.)*

Copy your directory from the previous exercise to a new directory called `ex05`

```terminal
$ cp -r ex04 ex05
$ cd ex05
```

Update the `requirements.txt` file to have these contents:

```
Flask==1.0.2
redis==2.10.6
```

Update the `app.py` file to have these contents:

```python
from flask import Flask, request
from redis import Redis
import os

app = Flask(__name__)


TEMPLATE = '''
<p><strong>Hello {name}</strong><p>
<p>
    <form method="post">
        <input type="text" name="entry" />
        <input type="submit" name="Submit" />
    </form>
</p>
'''


@app.route('/', methods=['POST', 'GET'])
def root():
    r = Redis(os.getenv('REDIS_SERVER', 'my-redis'),
              socket_timeout=2)
    if request.method == 'POST':
        entry = request.form['entry']
        r.lpush('entries', entry)

    output = TEMPLATE.format(name=os.getenv('NAME'))
    for entry in r.lrange('entries', 0, 4):
        output += '<p>%s</p>' % entry.decode()
    return output


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
```

Build a new version of the application.

```terminal
$ docker build -t app:05 .
```

You can run your app, like in previous exercises.

```terminal
$ docker run -p 8000:8000 app:05
```

And connect to it at `http://127.0.0.1/` in your browser. *But since you don't have a Redis server to connect to, you'll get an error.* (The error should say something about `redis.exceptions.ConnectionError`.) Let's fix that.


*You're on your own now ...*

## Part 1

Figure out how to run a Redis container
  - in the background
  - with then name `my-redis`

## Part 2

Figure out how to run the app with a link to the `my-redis` container.

You'll know it's working if the error we saw above goes away.

[\_]({{ "/ex05-add-redis-solution/" | relative_url }})
