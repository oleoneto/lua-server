FROM python:latest
ENV PYTHONUNBUFFERED 1
RUN apt-get update

# Install some necessary dependencies.
RUN apt-get install -y swig libssl-dev dpkg-dev netcat

# Install the requirements. This is done early so the requirements
# don't need to be reinstalled every time something unrelated changes,
# which would otherwise happen due to the way Docker does image caching.
RUN pip install -U pip
ADD requirements.txt /code/
RUN pip install -Ur /code/requirements.txt

# Add the Dokku-specific files to their locations.
ADD misc /app/
ADD misc/dokku/* /code/

# Copy the code and collect static media.
# Using and S3 space for the files
WORKDIR /code
COPY . /code/
#RUN /code/manage.py collectstatic --noinput