FROM python:3.6.7

WORKDIR usr/scr/webapp

COPY requirement.txt .

RUN apt-get update && \
apt-get install -y apt-utils python3-pip python3-dev

RUN pip install --no-cache-dir -r requirement.txt

COPY . .
