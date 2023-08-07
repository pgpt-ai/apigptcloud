import requests
from apigptcloud import aichat
import json


def fake_login():
    url = "http://192.168.1.19:8000/api/auth/fake/login/?"
    headers = {
        'Cookie': 'csrftoken=ZiLjd99bZyA6Z3ryILAaFWgfpN7uymsS; sessionid=l7n4qu0iw1jkfs7cz7zj9sdeyaaa6p8y',
        'Cache-Control': 'no-cache',
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
    }
    data = {
        "shop_id": 4
    }
    return json.dumps(requests.post(url, headers=headers, json=data).json(), indent=2)