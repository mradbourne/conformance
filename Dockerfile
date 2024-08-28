FROM ubuntu:22.04

WORKDIR /conformance
COPY requirements.txt requirements.txt

RUN apt-get update
RUN apt-get install -y python3.10 python3-pip

RUN pip install -r requirements.txt
