#!/usr/bin/python3.8

import requests
import json

YCOauth = 'YCOauth'
folder_id = 'folder_id'

response = requests.post('https://iam.api.cloud.yandex.net/iam/v1/tokens', json={'yandexPassportOauthToken':YCOauth})
YCiamToken = json.loads(response.content)['iamToken']

response = requests.get('https://compute.api.cloud.yandex.net/compute/v1/instances/?folder_id=' + folder_id,
    headers={'Authorization': 'Bearer ' + YCiamToken},)


instances = json.loads(response.content)['instances']
for instance in instances:
    if instance['labels']['tags'] == "reddit-app":
        appserver = instance['networkInterfaces'][0]['primaryV4Address']['oneToOneNat']['address']
    elif instance['labels']['tags'] == 'reddit-db':
        dbserver = instance['networkInterfaces'][0]['primaryV4Address']['oneToOneNat']['address']
    else:
        print(instance['labels']['tags'] + ' not match')
output = '{' + '"app":{"hosts":{"appserver":{"ansible_host":"' + appserver + '"} } },"db":{"hosts":{"dbserver":{"ansible_host":"' + dbserver + '"} } } }'

file = open("inventory.json", "w")
file.write(output)
file.close()