import requests
from apigptcloud import aichat
import json


def fake_login():
    session = requests.Session()
    url = aichat.url + "/api/auth/fake/login/?"
    headers = aichat.global_headers.copy()
    headers['Content-Type'] = 'application/json'
    data = {
        "shop_id": 4
    }
    res = json.dumps(session.post(url, headers=headers, json=data).json(), indent=2)
    aichat.global_headers['Cookie'] = ("csrftoken=" + session.cookies.get_dict()['csrftoken']
                                       + ";" + "sessionid=" + session.cookies.get_dict()['sessionid'])
    return res
