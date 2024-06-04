import requests
from pgptai import claude


def create(model: str, messages, max_tokens: int = None, **kwargs):
    url = claude.api_base + "/messages"
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

    if 'stream' in kwargs and kwargs['stream']:
        def process():
            response = requests.post(url, headers=headers, json=data, stream=True).iter_lines()
            for chunk in response:
                if chunk:
                    parse = chunk.decode('utf-8')
                    if len(parse) > 0:
                        yield parse

        return process()
    else:
        return requests.post(url, headers=headers, json=data).json()
