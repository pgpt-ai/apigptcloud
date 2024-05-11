# ChatGLM API 调用方法

## 配置环境
```python
from apigptcloud import chatglm
chatglm.api_key = ""
chatglm.api_base = ""
```

## ChatCompletion
请求示例：
```python
res = chatglm.completions.create(
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"}
    ],
    temperature=1,
)
```
返回示例：
```json
{
    "model": "chatglm2-6b",
    "object": "chat.completion",
    "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Hello! I'm happy to assist you with any questions or concerns you may have. How can I help you today?"
      },
      "finish_reason": "stop"
    }
    ],
    "created": 1691728340,
    "usage": {
    "prompt_tokens": 8,
    "completion_tokens": 25,
    "total_tokens": 33
    }
}
```
