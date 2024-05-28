# GeminiAI API 调用方法

## 配置环境

```python
from pgpt import geminiai

geminiai.api_key = ""
geminiai.api_base = ""
```
如果不声明`geminiai.api_base`，则默认使用[gemini.pgpt.cloud](https://gemini.pgpt.cloud)端点，请将相应的API Key填入`geminiai.api_key`。


## Chat
请求示例：
```python
res = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "parts": [
                {
                    "text": "hi"
                },
            ]
        }
    ]
)
```

返回示例：
```json
{
    "message": "Hello, this message is from apigpt.cloud! How may I assist you today?"
}
```
