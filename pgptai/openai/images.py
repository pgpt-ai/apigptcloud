from pgptai import openai
import requests


def create(model, prompt, size: str = '1024x1024', n: int = 1, **kwargs):
    url = openai.api_base + "/images/generations"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': "Bearer " + openai.api_key
    }
    data = {
        "model": model,
        "prompt": prompt,
        "size": size,
        "n": n
    }
    for arg in kwargs:
        data[arg] = kwargs[arg]

    return requests.post(url, headers=headers, json=data).json()
