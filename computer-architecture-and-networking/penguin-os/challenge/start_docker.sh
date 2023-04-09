#!/bin/bash

docker build -t penguin-os . && \
docker run -it -p 20:20 -p 22:22 -p 2121:2121 -p 30000-30100:30000-30100 --name penguin-os-container --rm penguin-os