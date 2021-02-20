#!/bin/bash

CONTAINER="mbus-srv"
IMAGE="${CONTAINER}-img"
NETWORK="mbus-net"
PUB_PORT="-p 502:5020"


docker network create ${NETWORK}

docker build -t ${IMAGE} .

docker rm -f ${CONTAINER}

docker run -d --name ${CONTAINER} \
           --restart unless-stopped \
           --network ${NETWORK} \
           ${PUB_PORT} \
           ${IMAGE}