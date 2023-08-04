import requests
from apigptcloud import azure
import json


def create(messages: list, **kwargs):
    url = ("https://" + azure.resource_name + ".openai.azure.com/openai/deployments/" + azure.deployment_name +
           "/chat/completions?api-version=" + azure.api_version)
    headers = {
        'Content-Type': 'application/json',
        'api-key': azure.api_key
    }
    data = {
        "messages": messages,
    }
    # validate kwargs
    for arg in kwargs:
        data[arg] = kwargs[arg]

    return json.dumps(requests.post(url, headers=headers, json=data).json(), indent=2)
