#!/bin/bash

docker build -t mbus-srv-img .
docker run -d -t --name mbus-srv --restart always -p 502:5020 mbus-srv-img
