import requests
import json
import apigptcloud

api_key: str = ""

models = {
    "openai-chat": ['gpt-3.5-turbo', 'gpt-3.5-turbo-16k', 'gpt-4', 'gpt-4-32k', 'gpt-4-turbo', 'gpt-3.5-turbo-instruct',
                    'gpt-4-turbo-vision'],
    "openai-embeddings": ['text-embedding-ada-002'],
    "claude-completions": ['claude-1'],
    "stablediffusion": ["stablediffusion"],
    "audioai-speech": ["audioai-speech"],
    "audioai-transcriptions": ["audioai-transcriptions"],
    "textai": ["textai"],

}

reverse_models = {v: k for k, values in models.items() for v in values}


def create(model: str, **kwargs):
    # 检查模型名称是否存在
    # Check if model exists
    try:
        key = reverse_models[model]
    except KeyError as e:
        return {
            "status": 400,
            "msg": "Model not found",
        }
    # print("Now using "+key)

    if key == "openai-chat":
        apigptcloud.openai.api_key = api_key
        # 如果不是流式请求
        # If not stream request
        if not kwargs.get("stream", False):
            response_old = apigptcloud.openai.chat.completions.create(model, **kwargs)
            try:
                response_new: dict = {
                    "status": 200,
                    "msg": "success",
                    "data": {
                        "id": response_old["id"],
                        "model_type": response_old["object"],
                        "model": response_old["model"],
                        "messages": response_old["choices"][0]["message"]["content"],
                    }
                }
                return response_new

            except Exception as e:
                response_new: dict = {
                    "status": 400,
                    "msg": json.loads(response_old["error"]["message"]),
                }
                return response_new

        else:
            # print("6")
            response_old = apigptcloud.openai.chat.completions.create(model, **kwargs)
            def process():
                for i in response_old:
                    # print(i)
                    messages = i["choices"][0] if i["choices"] else None
                    messages = messages["delta"] if messages else None
                    response_new: dict = {
                        "status": 200,
                        "msg": "success",
                        "data": {
                            "model_type": i["object"],
                            "model": i["model"],
                            "messages": messages,
                        }
                    }
                    yield response_new
            return process()

    elif key == "openai-embeddings":
        apigptcloud.openai.api_key = api_key
        try:
            return apigptcloud.openai.embeddings.create(model, **kwargs)
        except Exception as e:
            return apigptcloud.openai.embeddings.create(model, **kwargs)

    elif key == "claude-completions":
        apigptcloud.claude.api_key = api_key
        # 如果不是流式请求
        # If not stream request
        if not kwargs.get("stream", False):
            response_old = apigptcloud.claude.completions.create(model, **kwargs)
            try:
                response_new: dict = {
                    "status": 200,
                    "msg": "success",
                    "data": {
                        "id": response_old["id"],
                        "model_type": response_old["type"],
                        "model": response_old["model"],
                        "messages": response_old["completion"],
                    }
                }
                return response_new
            except Exception as e:
                print(response_old)
                response_new: dict = {
                    "status": 400,
                    "msg": response_old,
                }
                return response_new
        else:
            response_old = apigptcloud.claude.completions.create(model, **kwargs)
            def process():
                for i in response_old:
                    print(i)
                    if "data" in i:
                        data = json.loads(i.split("data: ")[-1])
                        if not data["type"] == "ping":
                            response_new: dict = {
                                "status": 200,
                                "msg": "success",
                                "data": {
                                    "model_type": data["type"],
                                    "model": data["model"],
                                    "messages": data["completion"],
                                }
                            }
                            yield response_new
                    elif "value_error.missing" in i:
                        response_new: dict = {
                            "status": 400,
                            "msg": json.loads(i),
                        }
                        yield response_new
            result = process()
            return result

    elif key == "stablediffusion":
        apigptcloud.stablediffusion.api_key = api_key
        try:
            return apigptcloud.stablediffusion.draw.create(**kwargs)
        except Exception as e:
            return apigptcloud.stablediffusion.draw.create(**kwargs)

    elif key == "audioai-speech":
        apigptcloud.audioai.api_key = api_key
        try:
            return apigptcloud.audioai.speech.create(model, **kwargs)
        except Exception as e:
            return apigptcloud.audioai.speech.create(model, **kwargs)

    elif key == "audioai-transcriptions":
        apigptcloud.audioai.api_key = api_key
        try:
            return apigptcloud.audioai.transcriptions.create(model, **kwargs)
        except Exception as e:
            return apigptcloud.audioai.transcriptions.create(model, **kwargs)

    elif key == "textai":
        apigptcloud.textai.api_key = api_key
        try:
            return apigptcloud.textai.translations.create(model, **kwargs)
        except Exception as e:
            return apigptcloud.textai.translations.create(model, **kwargs)
