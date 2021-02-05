#!/bin/bash

docker build -t py-tk-hmi-img .
docker run -d --name py-tk-hmi \
           --restart=always \
           --network host \
           --volume /tmp/.X11-unix:/tmp/.X11-unix:ro \
           --volume $HOME/.Xauthority:/root/.Xauthority:rw \
           py-tk-hmi-img
