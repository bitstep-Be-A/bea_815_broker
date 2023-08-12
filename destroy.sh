#!/bin/bash

docker rm -f broker webserver
docker rmi broker nginx:alpine
