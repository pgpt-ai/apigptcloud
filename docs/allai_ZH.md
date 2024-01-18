# AllAI 调用方法

## 配置环境
请在`allai.api_key`中填入**相对应服务**的API Key
```python
from apigptcloud import allai
allai.api_key = ""
```

## 模型列表
通过输入模型的名称选择对应的服务，如下所示：
```json
{
    "openai-chat": ['gpt-3.5-turbo', 'gpt-3.5-turbo-16k', 'gpt-4', 'gpt-4-32k', 'gpt-4-turbo', 'gpt-3.5-turbo-instruct'],
    "openai-embeddings": ['text-embedding-ada-002'],
    "claude-completions": ['claude-1'],
    "stablediffusion": ["stablediffusion"],
    "audioai-speech": ["audioai-speech"],
    "audioai-transcriptions": ["audioai-transcriptions"],
    "textai": ["textai"]
}
```

## Chat
请求示例：  
```python
res = allai.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"}
    ],
    stream=False,
)
```
此时函数会自动调用`apigptcloud.openai.chat.completions.create()`