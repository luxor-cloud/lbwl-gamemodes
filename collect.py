#!/usr/bin/env python3

import json
import os
import zipfile
import urllib.request
import base64
import boto3
from concurrent import futures

def download_map(client, map):
  local_path = '.work/maps/{}.zip'.format(map['name'])
  key = 'lbwl/maps/flash/{}/v{}.zip'.format(map['name'], map['version'])
  with open(local_path, 'wb+') as file:
    client.download_fileobj('luxor', key, file)
  with zipfile.ZipFile(local_path, 'r') as zip_ref:
    zip_ref.extractall(local_path[:-4])

def download_all_maps(client, maps):
  with futures.ThreadPoolExecutor(max_workers=5) as executor:
    future_to_key = {executor.submit(download_map, client, map): map for map in maps}
    for future in futures.as_completed(future_to_key):
      key = future_to_key[future]
      exception = future.exception()
      if not exception:
        yield key, future.result()
      else:
        yield key, exception

def download_jar(nexus_host, nexus_user, nexus_passwd, mode_name, mode_version):
  url = 'http://{host}/repository/lbwl-mvn-releases/cloud/luxor/lbwl/{game}/{version}/{game}-{version}.jar'
  auth = base64.b64encode('{}:{}'.format(nexus_user, nexus_passwd).encode('utf-8')).decode('ascii')
  opener = urllib.request.build_opener()
  opener.addheaders = [('Authorization', 'Basic {}'.format(auth))]
  urllib.request.install_opener(opener)
  urllib.request.urlretrieve(
    url.format(host=nexus_host, game=mode_name, version=mode_version), 
    '.work/{}.jar'.format(mode_name)
  )

data = {}
with open('mode.json') as json_file:
  data = json.load(json_file)

work_dir = '.work'
maps_work_dir = '{}/maps'.format(work_dir)

do_region = os.environ['DO_REGION']
do_endpoint = os.environ['DO_ENDPOINT']
do_key_id = os.environ['DO_KEY_ID']
do_secret = os.environ['DO_SECRET']

nexus_host = os.environ['MVN_REPO_HOST']
nexus_user = os.environ['MVN_REPO_USER']
nexus_passwd = os.environ['MVN_REPO_PASSWORD']

mode_name = data['jar']['name']
mode_version = data['jar']['version']
  
os.mkdir('.work')
os.mkdir('.work/maps')

download_jar(
  nexus_host, 
  nexus_user, 
  nexus_passwd, 
  mode_name, 
  mode_version
)

client = boto3.session.Session().client(
  's3',
  region_name=do_region,
  endpoint_url=do_endpoint,
  aws_access_key_id=do_key_id,
  aws_secret_access_key=do_secret
)

# append spawn map to maps
data['maps'].append({ 'name': 'spawn', 'version': data['spawn']['version'] })

for key, result in download_all_maps(client, data['maps']):
  print('{}: {}'.format(key, result))
