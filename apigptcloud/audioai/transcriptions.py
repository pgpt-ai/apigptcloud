from apigptcloud import audioai
import requests


def create(model: str, file, language: str):

    if audioai.api_base == "":
        audioai.api_base = "https://ai.pgpt.cloud"

    url = f'{audioai.api_base}/v1/speech/speech2text'
    headers = {
        'accept': 'application/json',
        "Authorization": f"Bearer {audioai.api_key}"
    }
    data = {
        'lang': language,
    }
    files = [
        ('audio', ("file", file, "audio/"+file.name.split(".")[-1])),
    ]
    if language == "zh-CN":
        return requests.request("POST", url, headers=headers, params=data, files=files).json()
    elif language == "en-US":
        return requests.request("POST", url, headers=headers, data=data, files=files).json()
    else:
        return {
            "status": 400,
            "msg": "Language not supported",
        }
