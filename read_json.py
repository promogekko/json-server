#! /usr/bin/python3

import json
from urllib.request import urlopen

url = "http://localhost:5000/todo/api/v1.0/tasks"

response = urlopen(url)

data = json.loads(response.read().decode(response.info().get_param('charset') or 'utf-8'))

print(str(data))
