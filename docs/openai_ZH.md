# OpenAI API 调用方法

## 配置环境
```python
from apigptcloud import openai
openai.api_key = ""
openai.api_base = ""
```

## Chat
请求示例：
```python
res = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"}
    ],
    temperature=2,
)
```
返回示例：
```json
{
    "id":"chatcmpl-7SKQgp3ry5w9ZB0A3mMcvYOFB1VYG",
    "object":"chat.completion",
    "created":1686986070,
    "model":"gpt-35-turbo",
    "choices":[
        {
            "index":0,
            "finish_reason":"stop",
            "message":{
                "role":"assistant",
                "content":"Hello, this message is from apigpt.cloud! How may I assist you today?"
            }
        }
    ],
    "usage":{
        "completion_tokens":18,
        "prompt_tokens":18,
        "total_tokens":36
    }
}
```

## Completion
Compeletion 已在 2024 年 1 月 4 日被废弃。请使用 `gpt-3.5-turbo-instruct` 模型作为替代。使用方法与 Chat 相同。

## Embedding
请求示例：
```python
res = openai.embeddings.create(
    model="gpt-3.5-turbo",
    input="The food was delicious and the waiter..."
)
```
返回示例：
```json
{
  "object": "embedding",
  "embedding": [
    0.0023064255,
    -0.009327292,
    .... (1536 floats total for ada-002)
    -0.0028842222,
  ],
  "index": 0
}
```