import requests
from apigptcloud import claude
import json


def create(model: str, prompt: str, **kwargs):
    url = claude.api_base
    headers = {
        'Content-Type': 'application/json',
        'x-api-key': claude.api_key
    }
    data = {
        "model": model,
        "prompt": prompt,
    }
    for arg in kwargs:
        data[arg] = kwargs[arg]

    return requests.post(url, headers=headers, json=data).json()
