#!/bin/bash

docker build -t skipperscookie-80 . && \
docker run -it -p 80:80 --rm --name skipperscookie-container skipperscookie-80