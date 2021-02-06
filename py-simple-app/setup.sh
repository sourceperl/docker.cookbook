#!/bin/bash

#docker rm -f py-simple-app
docker build -t py-simple-app-img .
docker run --name py-simple-app --restart no py-simple-app-img
