import requests
from apigptcloud import geminiai


def create(model, contents, stream=False, **kwargs):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f'Bearer {geminiai.api_key}'
    }
    chat_url = f'{geminiai.api_base}/chat/completions'
    payload = {
        "model": model,
        "contents": contents,
        **kwargs
    }
    if stream:
        def process():
            try:
                payload['stream'] = True
                response = requests.post(chat_url, headers=headers, json=payload, stream=True).iter_lines()
            except Exception as e:
                return {"error": {"message": str(e)}}
            for chunk in response:
                if chunk:
                    parse = chunk.decode('utf-8')
                    if parse == "[DONE]":
                        break
                    yield parse
        return process()
    res = requests.post(chat_url, json=payload, headers=headers)
    if not res:
        return {"error": {"message": "No response received"}}
    return res.json()
