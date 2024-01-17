from apigptcloud import speech
import requests


def speech_2_text_wav(filename: str, filepaths: str, lang: str):
    """
    """
    url = f'{speech.api_base}/v1/speech/speech2text'
    headers = {
        'accept': 'application/json',
        "Authorization": f"Bearer {speech.api_key}"
    }
    data = {
        'lang': lang,
    }
    files = [
        ('audio', (filename, open(filepaths, 'rb'), 'audio/wav')),
    ]
    if lang == "zh-CN":
        return requests.request("POST", url, headers=headers, params=data, files=files).json()
    elif lang == "en-US":
        return requests.request("POST", url, headers=headers, data=data, files=files).json()
    else:
        raise Exception("Language not supported")


def speech_2_text_amr(filename: str, filepaths: str, lang: str):
    """
    """
    url = f'{speech.api_base}/v1/speech/speech2text'
    headers = {
        'accept': 'application/json',
        "Authorization": f"Bearer {speech.api_key}"
    }
    data = {
        'lang': lang,
    }
    files = [
        ('audio', (filename, open(filepaths, 'rb'), 'audio/amr')),
    ]
    if lang == "zh-CN":
        return requests.request("POST", url, headers=headers, params=data, files=files).json()
    elif lang == "en-US":
        return requests.request("POST", url, headers=headers, data=data, files=files).json()
    else:
        raise Exception("Language not supported")
