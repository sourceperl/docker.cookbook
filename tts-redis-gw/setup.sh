#!/bin/bash

CONTAINER="tts-redis-gw"
IMAGE="${CONTAINER}-img"

docker rm -f ${CONTAINER}

docker build -t ${IMAGE} .

docker run -t --name ${CONTAINER} \
           --restart no \
           --device /dev/snd \
           --env PULSE_SERVER=unix:${XDG_RUNTIME_DIR}/pulse/native \
           --volume ${XDG_RUNTIME_DIR}/pulse/native:${XDG_RUNTIME_DIR}/pulse/native \
           --volume /home/pi/.config/pulse/cookie:/root/.config/pulse/cookie \
           --group-add audio \
           --network redis-net \
           ${IMAGE}
