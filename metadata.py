#!/usr/bin/env python3

import argparse
import json
from checksumdir import dirhash

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
  sha1hash = dirhash(args.update, 'sha1', excluded_files=['collect.py', 'Dockerfile'], ignore_hidden=True)
  with open('.metadata', 'r+') as json_file:
    data = json.load(json_file)
    data[args.update] = sha1hash
    json_file.seek(0)
    json.dump(data, json_file, indent=2)
    json_file.truncate()

if args.rev:
  with open('.metadata', 'r') as json_file:
    data = json.load(json_file)
    print(data[args.rev])

if args.mode_version:
  print(read_mode_file(args.mode_version)['version'])
