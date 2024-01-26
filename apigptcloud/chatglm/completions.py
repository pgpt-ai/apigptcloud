import requests
from apigptcloud import chatglm
import json


def create(model: str, messages: list, **kwargs):
    url = chatglm.api_base
    headers = {
        'Content-Type': 'application/json',
        'Authorization': "Bearer " + chatglm.api_key
    }
    data = {
        "messages": messages,
    }
    for arg in kwargs:
        data[arg] = kwargs[arg]

    return requests.post(url, headers=headers, json=data).json()
