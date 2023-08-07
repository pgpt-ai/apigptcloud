import requests
from apigptcloud import aichat
import json


def pdf(file_path: str, integration_id: int):
    url = 'http://192.168.1.19:8000/api/pglearn/embedding/pdf/'
    headers = aichat.global_headers
    payload = {'integration_id': integration_id}
    files = [
        ('file', ('file', open(file_path, 'rb'), 'application/pdf'))
    ]
    return json.dumps(
        requests.request("POST", url, headers=headers, data=payload, files=files).json(), indent=2)


def txt(file_path: str, integration_id: int):
    url = 'http://192.168.1.19:8000/api/pglearn/embedding/txt/'
    headers = aichat.global_headers
    payload = {'integration_id': integration_id}
    files = [
        ('file', ('file', open(file_path, 'rb'), 'application/octet-stream'))
    ]
    return json.dumps(
        requests.request("POST", url, headers=headers, data=payload, files=files).json(), indent=2)
