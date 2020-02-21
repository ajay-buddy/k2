FROM python:3.7-alpine
MAINTAINER Ajay Yadav

ENV PYTHONUNBUFFERED 1

COPY ./requirments.txt /requirments.txt
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .temp-build-deps \
        gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /requirments.txt
RUN apk del .temp-build-deps
RUN pip install djangorestframework-simplejwt
RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user