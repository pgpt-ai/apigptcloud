import requests
import json
from pgptai import openai

supported_models = [
    'gpt-4o-mini', 'gpt-4o', 'gpt-o1-mini', 'deepseek-r1', 'deepseek-v3'
]


def create(model: str, messages: list, **kwargs):
    """
    函数接受一个模型名称和一个消息列表作为参数，以及其他可选的关键字参数。这些参数将被用于创建一个新的聊天完成请求。
    """

    # 检查OpenAI的API基础URL是否已经设置，如果没有，则设置为默认的URL。
    if openai.api_base == "":
        openai.api_base = "https://openai.pgpt.cloud/v1"

    # 构建请求的URL、头部信息和数据。头部信息包含了内容类型和授权信息，数据包含了模型名称和消息列表，以及其他可选的关键字参数。
    url = openai.api_base + "/chat/completions"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': "Bearer " + openai.api_key
    }
    data = {
        "model": model,
        "messages": messages,
    }
    for arg in kwargs:
        data[arg] = kwargs[arg]

    # 在发送请求之前，会检查提供的模型名称是否在支持的模型列表中。如果不在，函数将返回一个错误信息。
    if model not in supported_models:
        return {'detail': [{'loc': ['body', 'model'], 'msg': f"(local) value is not a valid enumeration member; permitted: {supported_models}", 'type': 'type_error.enum', 'ctx': {'enum_values': f"{supported_models}"}}]}
    else:
        # 如果模型名称有效，函数将检查是否需要使用流模式。如果需要，函数将创建一个生成器，该生成器会持续从服务器获取数据，直到接收到"[DONE]"消息为止。在这个过程中，每接收到一个数据块，就会尝试将其解析为JSON，并将结果yield出去。
        if 'stream' in kwargs and kwargs['stream']:
            # print("stream")
            def process():
                response = requests.post(url, headers=headers, json=data, stream=True).iter_lines()
                for chunk in response:
                    if chunk:
                        parse = chunk.decode('utf-8').split('data: ')[-1]
                        if parse == "[DONE]":
                            break
                        # try:
                        #     answer = json.loads(parse)
                        #     if len(answer) > 0:
                        #         yield answer
                        # except Exception as e:
                        #     yield parse
                        yield parse

            return process()
            # return response

        # 如果不需要使用流模式，函数将直接发送请求，并返回服务器的响应。
        else:
            # print("else")
            # print(json.dumps({
            #     "url": url,
            #     "headers": headers,
            #     "data": data
            # }, indent=2))
            return requests.post(url, headers=headers, json=data).json()
