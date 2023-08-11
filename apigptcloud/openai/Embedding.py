import requests
from apigptcloud import openai
import json


def create(model: str, input):
    url = openai.api_base + "/embeddings"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': "Bearer " + openai.api_key
    }
    data = {
        "model": model,
        "input": input,
    }
    return json.dumps(requests.post(url, headers=headers, json=data).json(), indent=2)

