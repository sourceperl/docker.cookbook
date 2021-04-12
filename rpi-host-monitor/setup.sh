#!/bin/bash

CONTAINER="rpi-host-monitor"
IMAGE="${CONTAINER}-img"

docker rm -f ${CONTAINER}
docker build -t ${IMAGE} .
docker run -d --name ${CONTAINER} \
           --restart unless-stopped \
	   --network influxdb-net \
	   --log-opt max-size=50m \
           ${IMAGE}
