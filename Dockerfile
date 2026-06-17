FROM python:3.10

WORKDIR /app

RUN apt-get update && apt-get install -y gcc libffi-dev libssl-dev && apt-get clean

COPY . .

RUN pip install -e .

EXPOSE 80

CMD ["uwsgi", "--ini", "app.ini"]
