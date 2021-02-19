#!/bin/bash

CONTAINER="mqtt-srv"
IMAGE="eclipse-mosquitto:1.6.13"
NETWORK="mqtt-net"
# PUB_PORT="-p 1883:1883"


docker network create ${NETWORK}

docker rm -f ${CONTAINER}

docker run -d --name ${CONTAINER} \
           --restart unless-stopped \
           --network ${NETWORK} \
           ${PUB_PORT} \
           ${IMAGE}
