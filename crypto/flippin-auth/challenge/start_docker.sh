#!/bin/bash

docker build -t flippinauth-3000 . && \
docker run -it -p 3000:3000 --rm --name flippinauth-container flippinauth-3000