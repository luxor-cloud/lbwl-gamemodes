#!/usr/bin/env python3

import json
import os
import pysftp
import zipfile
import urllib.request

def downloadAndUnzip(remote_path, local_path):
  print('DOWNLOAD > {}'.format(remote_path.format('spawn', data['spawn']['version'])))
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

storage_host = os.environ['MAP_STORAGE_HOST']
storage_user = os.environ['MAP_STORAGE_USER']
storage_passwd = os.environ['MAP_STORAGE_PASSWORD']

nexus_host = os.environ['MVN_REPO_HOST']
nexus_user = os.environ['MVN_REPO_USER']
nexus_passwd = os.environ['MVN_REPO_PASSWORD']

mode_name = data['jar']['name']
mode_version = data['jar']['version']

url = 'http://{user}:{passwd}@{host}/repository/lbwl-mvn-releases/cloud/luxor/lbwl/{game}/{version}/{game}-{version}.jar'
urllib.request.urlretrieve(url.format(user=nexus_user, passwd=nexus_passwd, game=mode_name, version=mode_version, '.work/{}-{}'.format(mode_name, mode_version))

with pysftp.Connection(host=storage_host, username=storage_user, password=storage_passwd, cnopts=cnopts) as sftp:
  remote_path = '/lbwl/maps/flash/{}/{}.zip'
  downloadAndUnzip(remote_path.format('spawn', data['spawn']['version']), '.work/spawn.zip')
  for v in data['maps']:
    path = remote_path.format(v['name'], v['version'])
    downloadAndUnzip(path, '.work/maps/{}.zip'.format(v['name']))
