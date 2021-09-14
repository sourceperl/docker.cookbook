#!/bin/bash

CONTAINER="influxdb-srv"
IMAGE="influxdb:1.7.10"
NETWORK="influxdb-net"
DATA_VOLUME="influxdb-data-vol"
#PUB_PORT="-p 8086:8086"


docker network create ${NETWORK}
docker volume create ${DATA_VOLUME}

docker rm -f ${CONTAINER}

docker run -d --name ${CONTAINER} \
           --restart unless-stopped \
           --network ${NETWORK} \
           --volume ${DATA_VOLUME}:/var/lib/influxdb \
           --env INFLUXDB_DATA_ENGINE=tsm1 \
           --env INFLUXDB_REPORTING_DISABLED=true \
           --env INFLUXDB_DB=mydb \
           ${PUB_PORT} \
           ${IMAGE}
