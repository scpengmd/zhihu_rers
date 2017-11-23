# -*- coding:utf-8 -*-

import requests
import re
import json

#获得token值
headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/x-www-form-urlencoded',
}

data = [
  ('grant_type', 'password'),
  ('username', 'sasdemo01'),
  ('password', 'Shuchi2016'),
]

token_dict = requests.post('http://viyasrv/SASLogon/oauth/token', headers=headers, data=data, auth=('sas.ec', ''))
# print(token_dict.text)
acc=json.loads(token_dict.text)
token_value = (acc["access_token"])

# a = re.match('{"access_token":"(.*?)".*?', token_dict.text)
# token_value = (a.group(1))
# print(token_value)

#转入token值

headers2 = {
    'Content-Type': 'application/vnd.sas.microanalytic.module.step.input+json',
    'Accept': 'application/vnd.sas.microanalytic.module.step.output+json',
    'Authorization': 'Bearer ' + token_value,
}

data2 = '{"inputs": [{"name": "\\"id_\\"", "value": 20 }] }'

b = requests.post('http://viyasrv/SASMicroAnalyticService/modules/decision_test1031/steps/execute', headers=headers2, data=data2)
# print(b.text)


a = '\u5e10\u53f7\u6216\u5bc6\u7801\u9519\u8bef'
c = '123123123123123123'





