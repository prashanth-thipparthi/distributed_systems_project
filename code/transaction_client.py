import requests
import json

API_ENDPOINT = "http://127.0.0.1:5000/sendmoney"

data = {"receivers":["rahul","raghu"]}
body = json.dumps(data)
r = requests.post(url = API_ENDPOINT, data = body)

