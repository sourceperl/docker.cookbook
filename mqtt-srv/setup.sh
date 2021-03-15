#!/bin/bash

CONTAINER="mqtt-srv"
IMAGE="eclipse-mosquitto:2.0.9"
NETWORK="mqtt-net"
# PUB_PORT="-p 1883:1883"
CMD="mosquitto -c /mosquitto-no-auth.conf"


docker network create ${NETWORK}

docker rm -f ${CONTAINER}

docker run -d --name ${CONTAINER} \
           --restart unless-stopped \
           --network ${NETWORK} \
           ${PUB_PORT} \
           ${IMAGE} \
           ${CMD}
