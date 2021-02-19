#!/bin/bash

CONTAINER="py-simple-app"
IMAGE="${CONTAINER}-img"

# docker rm -f ${CONTAINER}
docker build -t ${IMAGE} .
docker run --rm -it --name ${CONTAINER} \
           --restart no \
           ${IMAGE}
