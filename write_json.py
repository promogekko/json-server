#! /usr/bin/python3

import requests
import json

url = "http://localhost:5000/todo/api/v1.0/tasks"
data = {'title': u'hme', 'description': u'Test Json_restAPI', 'done' : False }
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.post(url, data=json.dumps(data), headers=headers)

#url = "http://localhost:5000/api/comment"
#data = {"name" : "Justin", "email" : "justin.randall@usb.com", "ip_address" : "127.0.0.1",
#        "url" : "http://web.com",  "body" : "le test", "entry_id" : 1
#       }
#headers = {'Content-Type': 'application/json','Accept': 'text/plain' }
#try:
#    r = requests.post(url, data=json.dumps(data), headers=headers)
#    print(r)
#except:
#    print("r {}".format(r))
