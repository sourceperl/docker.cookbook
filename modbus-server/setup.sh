#!/bin/bash

docker build -t mbus-srv-img .
docker run -d --restart always -p 502:5020 --name=mbus-srv -t mbus-srv-img
