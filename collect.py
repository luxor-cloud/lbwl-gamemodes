#!/usr/bin/env python

import json
import os
import pysftp
import zipfile

def downloadAndUnzip(remote_path, local_path):
  print 'DOWNLOAD ' + remote_path.format('spawn', data['spawn']['version'])
  sftp.get(remote_path, local_path)
  with zipfile.ZipFile(local_path, 'r') as zip_ref:
    zip_ref.extractall(local_path[:-4])

data = {}
with open('mode.json') as json_file:
  data = json.load(json_file)

os.mkdir('.work')
os.mkdir('.work/maps')

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None 

host = os.environ['MAP_STORAGE_HOST']
user = os.environ['MAP_STORAGE_USER']
passwd = os.environ['MAP_STORAGE_PASSWORD']

# TODO: download game jar

with pysftp.Connection(host=host, username=user, password=passwd, cnopts=cnopts) as sftp:
  remote_path = '/lbwl/maps/flash/{}/{}.zip'
  downloadAndUnzip(remote_path.format('spawn', data['spawn']['version']), '.work/spawn.zip')
  for v in data['maps']:
    path = remote_path.format(v['name'], v['version'])
    downloadAndUnzip(path, '.work/maps/{}.zip'.format(v['name']))