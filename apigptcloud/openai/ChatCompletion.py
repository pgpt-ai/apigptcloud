import requests
from apigptcloud import openai
import json


def create(model: str, messages: list, **kwargs):
    url = openai.api_base + "/chat/completions"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': "Bearer " + openai.api_key
    }
    data = {
        "model": model,
        "messages": messages,
    }
    for arg in kwargs:
        data[arg] = kwargs[arg]

    return json.dumps(requests.post(url, headers=headers, json=data).json(), indent=2)
