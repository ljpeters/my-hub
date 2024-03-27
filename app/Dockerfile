# syntax=docker/dockerfile:1.4
FROM docker.io/library/python:slim-bullseye AS builder

RUN mkdir /app

WORKDIR /app

COPY requirements.txt /app
RUN pip3 install -r requirements.txt

COPY . /app

ENTRYPOINT ["python3"]
CMD ["app.py"]
#CMD tail -f /dev/null