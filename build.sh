#!/usr/bin/env bash

set -e
docker login $DOCKER_REPO_URL -u $DOCKER_REPO_USER -p $DOCKER_REPO_PASSWORD

for d in */ ; do
  mode=$(basename $d)
  ver=$(./metadata.py --mode-version $mode)
  echo "INFO lbwl-$mode v$ver"
  tag=$DOCKER_REPO_URL/lbwl-$mode:$ver
  sudo chmod o+x /etc/docker
  exists=$(docker manifest inspect $tag > /dev/null ; echo $?)
  if [ $exists == 1 ]; then
    cd $d
    ./collect.py
    cd ..
    docker build -t $tag -f $mode/Dockerfile $d
    docker push $tag
  else 
    echo "INFO lbwl-$mode v$ver already exists, not updating"
  fi
done
