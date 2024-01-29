import requests
from apigptcloud import claude


def create(model: str, messages, max_tokens: int, **kwargs):
    url = claude.api_base + "messages"
    headers = {
        'Content-Type': 'application/json',
        'x-api-key': claude.api_key,
        'anthropic-version': '2023-06-01',
        'anthropic-beta': 'messages-2023-12-15'
    }
    data = {
        "model": model,
        "max_tokens": max_tokens,
        "messages": messages,
    }
    for arg in kwargs:
        data[arg] = kwargs[arg]

    print(data)

    return requests.post(url, headers=headers, json=data).json()