import requests
from apigptcloud import aichat
import json


def openai(query: str, integration_id: int):
    url = aichat.url + "/api/pgcompletion/document/chat/"
    headers = aichat.global_headers
    payload = {'integration_id': integration_id, 'query': query, 'llm': 'openai'}
    return json.dumps(requests.request("POST", url, headers=headers, data=payload), indent=2)


def chatglm(query: str, integration_id: int):
    url = aichat.url + "/api/pgcompletion/document/chat/"
    headers = aichat.global_headers
    payload = {'integration_id': integration_id, 'query': query, 'llm': 'chatglm'}
    return json.dumps(requests.request("POST", url, headers=headers, data=payload), indent=2)