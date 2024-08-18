FROM python:3.10

WORKDIR /app

ENV PYTHONPATH=/app/src

RUN apt-get update && apt-get install -y gcc libffi-dev libssl-dev && apt-get clean

RUN pip install --no-cache-dir flask flask-socketio gevent uwsgi

COPY . .

EXPOSE 80

CMD ["uwsgi", "--ini", "app.ini"]