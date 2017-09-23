#! /usr/bin/python3

import requests
import json

url = "http://localhost:5000/todo/api/v1.0/tasks"
data = {'title': u'Bob', 'description': u'We did it!', 'done' : False }
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.post(url, data=json.dumps(data), headers=headers)