#!/usr/bin/env bash

docker login docker.luxor.cloud -u test -p test

for d in */ ; do
  mode=$(basename $d)
  ver=$(./metadata.py --mode-version $mode)
  exists=$(docker manifest inspect lbwl-$mode:$ver > /dev/null ; echo $?)
  echo $exists
done
