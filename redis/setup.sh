#!/bin/bash

CONTAINER="redis-srv"
IMAGE="redis"
NETWORK="redis-net"
DATA_VOLUME="redis-data-vol"
PUB_PORT="-p 6379:6379"


docker network create ${NETWORK}
docker volume create ${DATA_VOLUME}

docker rm -f ${CONTAINER}

docker run -d --name ${CONTAINER} \
           --restart unless-stopped \
           --network ${NETWORK} \
           --mount source=${DATA_VOLUME},target=/data \
           ${PUB_PORT} \
           ${IMAGE}
