#!/bin/bash

CONTAINER="grafana-srv"
IMAGE="grafana/grafana:latest"
NETWORK="influxdb-net"
DATA_VOLUME="grafana-data-vol"
PUB_PORT="-p 0.0.0.0:3000:3000"


[[ $NETWORK ]] && docker network create ${NETWORK}
[[ $DATA_VOLUME ]] && docker volume create ${DATA_VOLUME}

docker rm -f ${CONTAINER}

docker create --name ${CONTAINER} \
              --restart unless-stopped \
              --volume ${DATA_VOLUME}:/var/lib/grafana \
              ${PUB_PORT} \
              ${IMAGE}

[[ $NETWORK ]] && docker network connect ${NETWORK} ${CONTAINER}

docker start ${CONTAINER}

echo "login to http://localhost:3000/ with admin/admin"
echo "add InfluxDB data sources with url=http://influxdb-srv:8086 and Database=mydb"
