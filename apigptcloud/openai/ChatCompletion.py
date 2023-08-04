import requests
from apigptcloud import openai
import json

valid_args = ["temperature", "stream", "max_tokens"]


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
    # validate kwargs
    for arg in kwargs:
        if arg not in valid_args:
            raise ValueError(f"Invalid argument: {arg}")
        else:
            if arg == "temperature":
                if isinstance(kwargs[arg], float):
                    data["temperature"] = kwargs[arg]
            elif arg == "stream":
                if isinstance(kwargs[arg], bool):
                    data["stream"] = kwargs[arg]
            elif arg == "max_tokens":
                if isinstance(kwargs[arg], int):
                    data["max_tokens"] = kwargs[arg]

    return json.dumps(requests.post(url, headers=headers, json=data).json(), indent=2)

