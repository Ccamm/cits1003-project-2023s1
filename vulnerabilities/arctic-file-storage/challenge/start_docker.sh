#!/bin/bash

docker build -t arcticfilestorage-3000 . && \
docker run -it -p 3000:3000 --rm --name arcticfilestorage-container arcticfilestorage-3000