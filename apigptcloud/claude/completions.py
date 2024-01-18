import requests
from apigptcloud import claude


def create(model: str, prompt: str, **kwargs):

    if claude.api_base == "":
        claude.api_base = "https://claude.pgpt.cloud/v1/"

    url = claude.api_base + "complete"
    headers = {
        'Content-Type': 'application/json',
        'x-api-key': claude.api_key
    }
    data = {
        "model": model,
        "prompt": prompt,
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
