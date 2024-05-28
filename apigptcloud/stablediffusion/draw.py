import requests
from apigptcloud import stablediffusion
import json


def create(prompt: str, quantity: int = 1, size: str = "16:9", **kwargs):
    url = stablediffusion.api_base
    headers = {
        'accept': 'application/json',
        "Authorization": "Bearer " + stablediffusion.api_key
    }
    data = {
        "prompt": prompt,
        "quantity": quantity,
        "size": size
    }
    for arg in kwargs:
        data[arg] = kwargs[arg]
    return requests.post(url + '/draw', headers=headers, json=data).json()
