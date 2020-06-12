#!/usr/bin/env python3

import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('--mode-version')
args = parser.parse_args()

def read_mode_file(mode):
  with open('{}/mode.json'.format(mode), 'r') as json_file:
    data = json.load(json_file)
    return data

if args.mode_version:
  print(read_mode_file(args.mode_version)['version'])
