import requests
from apigptcloud import aichat
import json


def fake_login():
    url = "http://192.168.1.19:8000/api/auth/fake/login/?"
    headers = aichat.global_headers
    headers['Content-Type'] = 'application/json'
    data = {
        "shop_id": 4
    }
    return json.dumps(requests.post(url, headers=headers, json=data).json(), indent=2)