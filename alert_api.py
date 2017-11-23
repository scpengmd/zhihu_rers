# -*- coding:utf-8 -*-

import requests
import json

#获得token值
headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/x-www-form-urlencoded',
}

data = [
  ('grant_type', 'password'),
  ('username', 'viadmin'),
  ('password', 'Shuchi2016'),
]

token_dict = requests.post('http://viyavi/SASLogon/oauth/token', headers=headers, data=data, auth=('sas.ec', ''))
acc=json.loads(token_dict.text)
token_value = (acc["access_token"])

print(token_value)

#转入token值

headers2 = {
    'Authorization': 'Bearer ' + token_value,
}

b = requests.post('http://viyavi/svi-vsd-service/deployments/runLatestForFlow/applyVsd', headers=headers2)
print(b.text)





