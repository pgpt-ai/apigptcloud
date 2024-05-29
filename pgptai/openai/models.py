import requests
from pgptai import openai


def list():
    url = openai.api_base + "/models"
    headers = {
        'Authorization': "Bearer " + openai.api_key
    }
    return requests.post(url, headers=headers).json()