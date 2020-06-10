#!/usr/bin/env bash

set -e

docker login $DOCKER_REPO_URL -u $DOCKER_REPO_USER -p $DOCKER_REPO_PASSWORD

for d in */ ; do
  mode=$(basename $d)
  ver=$(./metadata.py --mode-version $mode)
  
  echo "INFO lbwl-$mode v$ver"
  cd flash && ./collect.py && cd ..

  sudo chmod o+x /etc/docker
  exists=$(docker manifest inspect $DOCKER_REPO_URL/lbwl-$mode:$ver > /dev/null ; echo $?)
  if [ $exists == 0 ]; then
    tag=$DOCKER_REPO_URL/lbwl-$mode:$ver
    docker build -t $DOCKER_REPO_URL/$tag -f $dDockerfile $d
    docker push $tag
  else 
    echo "INFO lbwl-$mode v$ver already exists, not updating"
  fi
done
