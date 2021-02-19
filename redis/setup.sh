#!/bin/bash

docker network create redis-net

docker run -d --name redis-srv \
           --restart always \
           --network redis-net \
           redis
