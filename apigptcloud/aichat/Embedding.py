import requests
from apigptcloud import aichat
import json
import os


def pdf(file_path: str):
    url = aichat.api_base + "/v1/embeddings/"
    headers = {
        'Authorization': aichat.api_key
    }
    payload = {'type': 'pdf'}
    files = [
        ('file', (os.path.basename(file_path), open(file_path, 'rb'), 'application/pdf'))
    ]

    return json.dumps(
        requests.request("POST", url, headers=headers, data=payload, files=files).json(), indent=2)


def txt(file_path: str):
    url = aichat.api_base + "/v1/embeddings/"
    headers = {
        'Authorization': aichat.api_key
    }
    payload = {'type': 'txt'}
    files = [
        ('file', (os.path.basename(file_path), open(file_path, 'rb'), 'application/plain'))
    ]
    return json.dumps(
        requests.request("POST", url, headers=headers, data=payload, files=files).json(), indent=2)


def plain(text: str):
    url = aichat.api_base + "/v1/embeddings/"
    headers = {
        'Authorization': aichat.api_key
    }
    payload = {'type': 'plain', 'text': text}
    return json.dumps(
        requests.request("POST", url, headers=headers, data=payload).json(), indent=2)
