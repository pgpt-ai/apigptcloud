import requests
from apigptcloud import openai


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
    return requests.post(url, headers=headers, json=data).json()

