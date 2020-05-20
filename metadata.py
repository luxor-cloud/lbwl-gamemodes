#!/usr/bin/env python3

import argparse
import json
from checksumdir import dirhash

parser = argparse.ArgumentParser()
parser.add_argument('--update')
parser.add_argument('--mode')
args = parser.parse_args()

if args.update:
  sha1hash = dirhash(args.update, 'sha1', excluded_files=['collect.py'], ignore_hidden=True)
  with open('.metadata', 'r+') as json_file:
    data = json.load(json_file)
    data[args.update] = sha1hash
    json_file.seek(0)
    json.dump(data, json_file, indent=2)
    json_file.truncate()

if args.mode:
  with open('.metadata', 'r') as json_file:
    data = json.load(json_file)
    print(data[args.mode])
