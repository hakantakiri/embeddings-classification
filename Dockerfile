FROM ubuntu:20.04
FROM python:3.9

RUN apt update

# Coyping code
WORKDIR /opt/app
# COPY requirements.txt requirements.txt

# Installing python dependencies
# RUN pip3 install --no-cache-dir -r requirements.txt
CMD ["tail", "-f", "/dev/null"]
COPY . .