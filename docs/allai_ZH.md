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
    "openai-chat": ["gpt-3.5-turbo", "gpt-3.5-turbo-16k", "gpt-4", "gpt-4-32k", "gpt-4-turbo", "gpt-3.5-turbo-instruct"],
    "openai-embeddings": ["text-embedding-ada-002"],
    "claude-completions": ["claude-1"],
    "stablediffusion": ["stablediffusion"],
    "audioai-speech": ["audioai-speech"],
    "audioai-transcriptions": ["audioai-transcriptions"],
    "textai": ["textai"]
}
```

## 一般请求
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

返回示例（成功）：
```json
{
    "status": 200,
    "msg": "success",
    "data": {
        "id": "chatcmpl-8k1R63z46orIg2xSlTGRuzQ7FqPDq",
        "model_type": "chat.completion",
        "model": "gpt-3.5-turbo",
        "messages": "Hello! How can I assist you today?"
    }
}
```
返回示例（失败）：
```json
{
    "status": 400,
    "msg": {...}
}
```

## 流式请求
返回示例（成功）：
```json
{
  "status": 200, 
  "msg": "success", 
  "data": {
    "model_type": "chat.completion.chunk", "model": "gpt-35-turbo", "messages": "Hello"
  }
}
```
返回示例（失败）：
```json
{
  "status": 400, 
  "msg": "..."
}
```