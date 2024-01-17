from apigptcloud import audioai
import requests


def create(model: str, file, lang: str):
    """
    """
    url = f'{audioai.api_base}/v1/speech/speech2text'
    headers = {
        'accept': 'application/json',
        "Authorization": f"Bearer {audioai.api_key}"
    }
    data = {
        'lang': lang,
    }
    files = [
        ('audio', ("file", file, "audio/"+file.name.split(".")[-1])),
    ]
    if lang == "zh-CN":
        return requests.request("POST", url, headers=headers, params=data, files=files).json()
    elif lang == "en-US":
        return requests.request("POST", url, headers=headers, data=data, files=files).json()
    else:
        raise Exception("Language not supported")
