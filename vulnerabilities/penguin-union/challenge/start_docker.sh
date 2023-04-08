#!/bin/bash

docker build -t penguinunion-1337 . && \
docker run -it -p 1337:1337 --rm --name penguinunion-container penguinunion-1337