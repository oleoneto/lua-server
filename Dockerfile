# Base image
FROM python:3.7-slim-stretch

# Working directory
WORKDIR /code

# Environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8

# Copy dependencies
COPY requirements.txt .requirements
COPY notify.sh /code/.notify.sh

# Install dependencies
RUN apt-get update \
    && apt-get install -y \
    swig libssl-dev dpkg-dev \
    && chmod +x .notify.sh \
    && pip install -U pip gunicorn \
    && pip install -r .requirements


# Copy file structure to docker image
COPY . .

# Switch users
RUN groupadd -r docker && useradd --no-log-init -r -g docker docker
USER docker