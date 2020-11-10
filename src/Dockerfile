# Use Python 3 Docker Community image
FROM python:3

# Copy files to the container
COPY . ./app

# Change the working directory to /app
WORKDIR /app

# Install the required python packages
RUN python -m pip install -r requirements.txt

# Run uwsgi with the configuration in the .ini file
CMD ["uwsgi","--ini","hello.ini"]

# Expose the container to host
EXPOSE 80
