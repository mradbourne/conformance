#!/bin/bash
if ! command -v docker &> /dev/null
then
    echo "Opening in a container requires Docker but it is not installed."
    echo "Please install Docker and try again."
    exit 1
fi
if ! docker stats --no-stream &> /dev/null
then
    echo "Docker is not running. Please start Docker and try again."
    exit 1
fi
docker build --platform linux/amd64 -f Containerfile -t conformance:latest .
docker run --platform linux/amd64 --rm -v .:/conformance -it conformance:latest
