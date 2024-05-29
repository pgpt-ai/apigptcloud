# AllAI 调用方法

## 配置环境
请在`AllAI()`中填入**相对应服务**的API Key

```python
from pgptai import AllAI

client = AllAI(api_key='<YOUR API KEY>')
```

## 模型列表
通过输入模型的名称选择对应的服务，支持的模型如下：

### OpenAI
- gpt-3.5-turbo
- gpt-3.5-turbo-16k
- pgt-3.5-ultra
- gpt-4
- gpt-4-32k
- gpt-4-turbo
- gpt-4-turbo-vision
- pgt-4-ultra
- dall-e-2
- dall-e-3

### Claude
- claude-instant-1.2
- claude-2
- claude-3

### Gemini
- gemini-pro
- gemini-pro-vision

### stable Diffusion
- stable_diffusion

### ChatGLM
- chatglm2
- chatglm3


## 一般请求
请求示例：

```python
from pgptai import AllAI

client = AllAI(api_key='<YOUR API KEY>')

res = client.chat.completions.create(
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
    "msg": "succeed",
    "data": {
        "model_type": "chat.completion",
        "model": "gpt-3.5-turbo",
        "response": {
          "text": "Hello! How can I assist you today?"
        } 
    }
}
```
返回示例（失败）：
```json
{
    "status": 400,
    "error": {
        "code": "",
        "message": ""
    },
    "msg": "failed"
}
```

## 流式请求
返回示例（成功）：
```json
{
  "status": 200, 
  "msg": "success", 
  "data": {
    "model_type": "chat.completion.chunk", "model": "gpt-35-turbo", "response": {"text": "hello"}
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
