import requests
import openai
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
                data["temperature"] = arg
            if arg == "stream":
                data["stream"] = arg
            if arg == "max_tokens":
                data["max_tokens"] = arg
    return json.dumps(requests.post(url, headers=headers, json=data).json(), indent=2)

