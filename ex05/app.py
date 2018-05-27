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
