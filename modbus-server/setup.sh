#!/bin/bash

docker build -t mbus-srv .
docker run -d --restart always -p 502:5020 -t mbus-srv
