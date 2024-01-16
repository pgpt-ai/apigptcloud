# Compeletion was deprecated on January 4th, 2024.
import requests
from apigptcloud import openai


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
