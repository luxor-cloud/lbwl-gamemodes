#!/usr/bin/env bash

# $1 image name
# $2 image version
# $3 dockerfile folder

tag=$DOCKER_REPO_URL/$1:$2

docker build -t $tag -f $3/Dockerfile $3
docker push $tag
