import requests
from apigptcloud import openai

supported_models = [
    'gpt-3.5-turbo', 'gpt-3.5-turbo-16k', 'gpt-4', 'gpt-4-32k', 'gpt-4-turbo', 'gpt-3.5-turbo-instruct'
]


def create(model: str, messages: list, **kwargs):
    url = openai.api_base + "/chat/completions"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': "Bearer " + openai.api_key
    }
    data = {
        "model": model,
        "messages": messages,
    }
    for arg in kwargs:
        data[arg] = kwargs[arg]

    if model not in supported_models:
        return {'detail': [{'loc': ['body', 'model'], 'msg': "value is not a valid enumeration member; permitted: 'gpt-3.5-turbo', 'gpt-3.5-turbo-16k', 'gpt-4', 'gpt-4-32k', 'gpt-4-turbo', 'gpt-3.5-turbo-instruct'", 'type': 'type_error.enum', 'ctx': {'enum_values': ['gpt-3.5-turbo', 'gpt-3.5-turbo-16k', 'gpt-4', 'gpt-4-32k', 'gpt-4-turbo', 'gpt-3.5-turbo-instruct']}}]}

    return requests.post(url, headers=headers, json=data).json()