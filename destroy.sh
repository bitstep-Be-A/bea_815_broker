#!/bin/bash

docker rm -f publisher webserver
docker rmi publisher nginx:alpine
