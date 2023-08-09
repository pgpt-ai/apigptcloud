import requests
from apigptcloud import aichat
import json


def openai(query: str):
    url = aichat.api_base + "/v1/chat/completions/"
    headers = {
        'Authorization': aichat.api_key
    }
    payload = {'query': query, 'llm': 'openai'}
    return requests.request("POST", url, headers=headers, data=payload).json()


def chatglm(query: str):
    url = aichat.api_base + "/v1/chat/completions/"
    headers = {
        'Authorization': aichat.api_key
    }
    payload = {'query': query, 'llm': 'chatglm'}
    return requests.request("POST", url, headers=headers, data=payload).json()