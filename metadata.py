#!/usr/bin/env python3

import argparse
import json
import hashlib
import os

parser = argparse.ArgumentParser()
parser.add_argument('--update')
parser.add_argument('--rev')
parser.add_argument('--mode-version')
args = parser.parse_args()

def read_mode_file(mode):
  with open('{}/mode.json'.format(mode), 'r') as json_file:
    data = json.load(json_file)
    return data

if args.update:
  ghasher = hashlib.sha1()  
  exclude = ['.work']
  for root, dirs, files in os.walk(args.update, topdown=True):
    # https://stackoverflow.com/questions/19859840/excluding-directories-in-os-walk
    dirs[:] = [d for d in dirs if d not in exclude]
    for name in files:
        if name == 'collect.py':
          continue
        if name == 'Dockerfile':
          continue
        file_name = os.path.join(root, name)
        fhasher = hashlib.sha1()
        with open(str(file_name), 'rb') as afile:
            buf = afile.read()
            fhasher.update(buf)
        ghasher.update(fhasher.digest())
  with open('.metadata', 'r+') as json_file:
    data = json.load(json_file)
    data[args.update] = ghasher.hexdigest()
    json_file.seek(0)
    json.dump(data, json_file, indent=2)
    json_file.truncate()

if args.rev:
  with open('.metadata', 'r') as json_file:
    data = json.load(json_file)
    print(data[args.rev])

if args.mode_version:
  print(read_mode_file(args.mode_version)['version'])
