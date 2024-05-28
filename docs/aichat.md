# AIChat API Usage

## Before you start...
Sign up at [pgpt.cloud](https://user.pgpt.cloud/login/) and get your api_key.

## Config

```python
from pgpt import aichat

aichat.api_key = ""
```

## Usage

### Embedding
To begin with, please upload your documents to our end for embedding. We currently support the following formats:
```python
# pdf，pass in the file path.
res = aichat.Embedding.pdf("test.pdf")

# txt，pass in the file path.
res = aichat.Embedding.txt("test.txt")

# pass in any string.
res = aichat.Embedding.plain("Hello, world!")

# excel，pass in the .xlsx file path.
res = aichat.Embedding.excel("test.xlsx")

# pass in the web page url.
res = aichat.Embedding.web("https://docs.apigpt.cloud/")

# word，pass in the .docx file path.
res = aichat.Embedding.word("test.docx")
```
Response example:
```json
{
    "errno": 0,
    "data": {},
    "msg": "success"
}
```

### Document Q&A

After that, you may now communicate with your AIChat assistant, who can retrieve info from your documents. You can choose from the following AIGC providers:
```python
res = aichat.Chat.openai("Introduce yourself.")

res = aichat.Chat.chatglm("Introduce yourself.")
```
Response example:
```json5
{
  'errno': 0, 
  'data': {'response': 'I am your personal AI assistant. I can help you with anything you need.'}, 
  'msg': 'success'
}
```