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

    return requests.request("POST", url, headers=headers, data=payload, files=files).json()


def txt(file_path: str):
    url = aichat.api_base + "/v1/embeddings/"
    headers = {
        'Authorization': aichat.api_key
    }
    payload = {'type': 'txt'}
    files = [
        ('file', (os.path.basename(file_path), open(file_path, 'rb'), 'application/plain'))
    ]
    return requests.request("POST", url, headers=headers, data=payload, files=files).json()


def plain(text: str):
    url = aichat.api_base + "/v1/embeddings/"
    headers = {
        'Authorization': aichat.api_key
    }
    payload = {'type': 'plain', 'text': text}
    return requests.request("POST", url, headers=headers, data=payload).json()


def excel(file_path: str):
    url = aichat.api_base + "/v1/embeddings/"
    headers = {
        'Authorization': aichat.api_key
    }
    payload = {'type': 'excel'}
    files = [('file', (os.path.basename(file_path), open(file_path, 'rb'),
                       'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'))]
    return requests.request("POST", url, headers=headers, data=payload, files=files).json()


def web(path: str):
    url = aichat.api_base + "/v1/embeddings/"
    headers = {
        'Authorization': aichat.api_key
    }
    payload = {'type': 'url', 'text': path}
    return requests.request("POST", url, headers=headers, data=payload).json()