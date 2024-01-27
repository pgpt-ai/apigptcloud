import json
import apigptcloud

api_key: str = ""

# 该字典将模型名称映射到对应的服务
models = {
    "openai-chat": ['gpt-3.5-turbo', 'gpt-3.5-turbo-16k', 'gpt-4', 'gpt-4-32k', 'gpt-4-turbo', 'gpt-3.5-turbo-instruct',
                    'gpt-4-turbo-vision'],
    "openai-embeddings": ['text-embedding-ada-002'],
    "chatglm": ['chatglm'],
    "claude-completions": ['claude-1'],
    "stablediffusion": ["stablediffusion"],
    "audioai-speech": ["audioai-speech"],
    "audioai-transcriptions": ["audioai-transcriptions"],
    "textai": ["textai"],

}

# 该字典将服务名称映射回模型名称。
reverse_models = {v: k for k, values in models.items() for v in values}


def create(model: str, **kwargs):
    """
    该函数将根据传入的模型名称，调用对应的服务
    """

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
                        # "id": response_old["id"],
                        "model_type": response_old["object"],
                        "model": response_old["model"],
                        "response": response_old["choices"][0]["message"]["content"],
                    }
                }
                return response_new

            except Exception as e:
                response_new: dict = {
                    "status": 400,
                    "msg": json.loads(response_old["error"]["message"]),
                }
                return response_new

        # 如果是流式请求
        # If stream request
        else:
            response_old = apigptcloud.openai.chat.completions.create(model, **kwargs)
            def process():
                for i in response_old:
                    # print(i)
                    try:
                        messages = i["choices"][0] if i["choices"] else None
                        messages = messages["delta"] if messages else None
                        messages = messages.get("content", None) if messages else None
                        response_new: dict = {
                            "status": 200,
                            "msg": "success",
                            "data": {
                                "model_type": i["object"],
                                "model": i["model"],
                                "response": messages,
                            }
                        }
                        yield response_new
                    except TypeError as e:
                        response_new: dict = {
                            "status": 400,
                            "msg": str(i),
                        }
                        yield response_new
            return process()

    elif key == "openai-embeddings":
        apigptcloud.openai.api_key = api_key
        response = apigptcloud.openai.embeddings.create(model, **kwargs)
        # print(response)
        try:
            new_response: dict = {
                "status": 200,
                "msg": "success",
                "data": {
                    "model_type": response["data"][0]["object"],
                    "model": response["model"],
                    "response": response["data"][0]["embedding"],
                }
            }
            return new_response

        except Exception as e:
            # print(e)
            new_response: dict = {
                "status": 400,
                "msg": response,
            }
            return new_response

    # 警告：未经测试，目前沿用上方openai-chat的逻辑
    # Warning: Not tested, currently using the logic of openai-chat above
    elif key == "chatglm":
        apigptcloud.chatglm.api_key = api_key
        response = apigptcloud.chatglm.completions.create(model, **kwargs)
        try:
            new_response: dict = {
                "status": 200,
                "msg": "success",
                "data": {
                    "model_type": response["object"],
                    "model": response["model"],
                    "response": response["choices"][0]["message"]["content"],
                }
            }
            return new_response

        except Exception as e:
            new_response: dict = {
                "status": 400,
                "msg": response,
            }
            return new_response

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
                        # "id": response_old["id"],
                        "model_type": response_old["type"],
                        "model": response_old["model"],
                        "response": response_old["completion"],
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

        # 如果是流式请求
        # If stream request
        else:
            response_old = apigptcloud.claude.completions.create(model, **kwargs)
            def process():
                for i in response_old:
                    # print(i)
                    if "data" in i:
                        data = json.loads(i.split("data: ")[-1])
                        if not data["type"] == "ping":
                            response_new: dict = {
                                "status": 200,
                                "msg": "success",
                                "data": {
                                    "model_type": data["type"],
                                    "model": data["model"],
                                    "response": data["completion"],
                                }
                            }
                            yield response_new
                    elif "value_error.missing" in i:
                        response_new: dict = {
                            "status": 400,
                            "msg": i,
                        }
                        yield response_new
            result = process()
            return result

    # 警告：未经测试
    # Warning: Not tested
    elif key == "stablediffusion":
        apigptcloud.stablediffusion.api_key = api_key
        response = apigptcloud.stablediffusion.draw.create(model, **kwargs)
        try:
            new_response: dict = {
                "status": 200,
                "msg": "success",
                "data": {
                    "model_type": response["object"],
                    "model": response["model"],
                    "response": response["urls"],
                }
            }
            return new_response
        except Exception as e:
            new_response: dict = {
                "status": 400,
                "msg": response,
            }
            return new_response

    elif key == "audioai-speech":
        apigptcloud.audioai.api_key = api_key
        response = apigptcloud.audioai.speech.create(model, **kwargs)
        try:
            new_response: dict = {
                "status": 200,
                "msg": "success",
                "data": {
                    "model_type": "audioai",
                    "model": "speech",
                    "response": response["url"],
                }
            }
            return new_response
        except Exception as e:
            # import traceback
            # print(traceback.format_exc())
            new_response: dict = {
                "status": 400,
                "msg": response["error"]["message"],
            }
            return new_response

    elif key == "audioai-transcriptions":
        apigptcloud.audioai.api_key = api_key
        response = apigptcloud.audioai.transcriptions.create(model, **kwargs)
        try:
            # print(response)
            new_response: dict = {
                "status": 200,
                "msg": "success",
                "data": {
                    "model_type": "audioai",
                    "model": "transcriptions",
                    "response": response["text"],
                }
            }
            return new_response
        except Exception as e:
            new_response: dict = {
                "status": 400,
            }
            if response["msg"] == "Language not supported":
                new_response["msg"] = response["msg"]
            else:
                new_response["msg"] = response
            return new_response

    elif key == "textai":
        apigptcloud.textai.api_key = api_key
        response = apigptcloud.textai.translations.create(model, **kwargs)
        print(response)
        try:
            new_response: dict = {
                "status": 200,
                "msg": "success",
                "data": {
                    "model_type": "textai",
                    "model": "translations",
                    "response": response["translations"],
                }
            }
            return new_response

        except Exception as e:
            new_response: dict = {
                "status": 400,
            }
            if "The target language is not valid." in response["error"]["message"]:
                new_response["msg"] = response["error"]["message"]
            else:
                new_response["msg"] = response
            return new_response
