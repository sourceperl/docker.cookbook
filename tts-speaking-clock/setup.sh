#!/bin/bash

docker rm -f tts-speaking-clock
docker build -t tts-speaking-clock-img .
docker run -t --name tts-speaking-clock \
           --restart no \
           --device /dev/snd \
           --env PULSE_SERVER=unix:${XDG_RUNTIME_DIR}/pulse/native \
           --volume ${XDG_RUNTIME_DIR}/pulse/native:${XDG_RUNTIME_DIR}/pulse/native \
           --volume /home/pi/.config/pulse/cookie:/root/.config/pulse/cookie \
           --group-add audio \
           tts-speaking-clock-img
