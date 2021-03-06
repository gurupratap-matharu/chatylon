# Pull base image
FROM python:3.8

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work dir
WORKDIR /code

# install requirements
COPY Pipfile Pipfile.lock /code/
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install pipenv && pipenv install --system

# copy project
COPY . /code/