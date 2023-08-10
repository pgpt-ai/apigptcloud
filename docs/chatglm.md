# ChatGLM API 调用方法

## 配置环境
```python
from apigptcloud import chatglm
chatglm.api_key = ""
chatglm.api_base = ""
```

## ChatCompletion
```python
res = chatglm.ChatCompletion.create(
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"}
    ],
    temperature=1,
)
```