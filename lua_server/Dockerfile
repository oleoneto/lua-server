FROM python:3.6.5

# Environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1



# Set working directory
WORKDIR /usr/src/application/



# Copy requirements to working directory
COPY ./requirements.txt .



# Copy start script
COPY ./start.sh .



# Install requirements
RUN pip install --upgrade pip
RUN pip install -r requirements.txt



# Copy project files
COPY . /usr/src/application/



# Expose port NUMBER to allow communication to/from server
EXPOSE 80
EXPOSE 8000


# Specify start script
ENTRYPOINT ["/bin/bash", "/usr/src/application/start.sh"]
