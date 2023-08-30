import requests
from apigptcloud import openai
import json


def create(model: str, prompt: str, **kwargs):
    url = openai.api_base + "/completions"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': "Bearer " + openai.api_key
    }
    data = {
        "model": model,
        "prompt": prompt,
    }
    for arg in kwargs:
        data[arg] = kwargs[arg]

    return requests.post(url, headers=headers, json=data).json()
