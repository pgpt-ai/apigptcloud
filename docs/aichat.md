# AIChat API 调用方法

## 准备
前往[apigpt.cloud](https://apigpt.cloud/)注册账号，获取api_key。

## 配置环境
```python
from apigptcloud import aichat
aichat.api_key = ""
```

## 如何使用

### Embedding

首先，请将您的文档提供给我们的AIChat模型进行Embedding。 我们支持以下多种格式：
```python
# pdf 格式，传入文件路径。
res = aichat.Embedding.pdf("test.pdf")

# txt 格式，传入文件路径。
res = aichat.Embedding.txt("test.txt")

# 传入字符串。
res = aichat.Embedding.plain("Hello, world!")

# excel 格式，传入.xlsx文件路径。
res = aichat.Embedding.excel("test.xlsx")

# 传入网页链接。
res = aichat.Embedding.web("https://docs.apigpt.cloud/")

# word 格式，传入.docx文件路径。
res = aichat.Embedding.word("test.docx")
```
返回示例：
```json
{
    "errno": 0,
    "data": {},
    "msg": "success"
}
```

### 文档问答

待embedding结束后，您可以与AIChat助手进行交互式文档问答。您可以通过以下接口选择我们所支持的AIGC提供商：
```python
res = aichat.Chat.openai("这个网站是关于什么的？")

res = aichat.Chat.chatglm("这个文章写了什么？")
```
返回示例：
```json5
{
  'errno': 0, 
  'data': {'response': '我是一个语言模型AI助手，如果你有任何问题或需要帮助，请随时告诉我！'}, 
  'msg': 'success'
}
```