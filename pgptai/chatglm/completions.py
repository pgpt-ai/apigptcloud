import requests
from pgptai import chatglm
import json


def create(model: str, messages: list, **kwargs):
    url = chatglm.api_base + '/chat/completions'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': "Bearer " + chatglm.api_key
    }
    data = {
        "model": model,
        "messages": messages,
    }
    for arg in kwargs:
        data[arg] = kwargs[arg]

    return requests.post(url, headers=headers, json=data).json()
