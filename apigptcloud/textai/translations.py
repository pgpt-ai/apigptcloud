import requests
from apigptcloud import textai


def create(model: str, language: list, text: str):
    url = f"{textai.api_base}/v1/translate/"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {textai.api_key}",
    }
    data = {
        "to_lang": language,
        "text": text,
    }
    return requests.post(url, headers=headers, json=data).json()


def list():
    url = f"{textai.api_base}/v1/language/"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {textai.api_key}",
    }
    return requests.post(url, headers=headers).json()
