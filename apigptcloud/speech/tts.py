from apigptcloud import speech
import requests


def text_2_speech(voice_name: str, text: str):
    """
    """
    url = f'{speech.api_base}/v1/speech/text2speech'
    headers = {
        'accept': 'application/json',
        "Authorization": f"Bearer {speech.api_key}"
    }
    data = {
        'voice_name': voice_name,
        'text': text,
    }
    return requests.post(url, headers=headers, json=data).json()


def text_2_speech_voices():
    url = f'{speech.api_base}/v1/speech/text2speech/voices'
    headers = {
        'accept': 'application/json',
        "Authorization": f"Bearer {speech.api_key}"
    }
    return requests.request("POST", url, headers=headers).json()
