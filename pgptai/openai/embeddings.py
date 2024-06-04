import requests
from pgptai import openai


def create(model: str, input):

    if openai.api_base == "":
        openai.api_base = "https://openai.pgpt.cloud/v1"

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

