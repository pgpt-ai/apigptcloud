import requests
from apigptcloud import chatglm
import json

def create(messages: list, **kwargs):
    url = openai.api_base + "/chat/completions"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': "Bearer " + chatglm.api_key
    }
    data = {
        "messages": messages,
    }
    for arg in kwargs:
        data[arg] = kwargs[arg]

    return json.dumps(requests.post(url, headers=headers, json=data).json(), indent=2)
