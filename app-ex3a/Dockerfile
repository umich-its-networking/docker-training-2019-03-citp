FROM python:3.6-slim

COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt

WORKDIR /usr/src/app
ADD . /usr/src/app

EXPOSE 8000

ENV FLASK_DEBUG 1

CMD ["python", "app.py"]
