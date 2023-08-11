# OpenAI API 调用方法

## 配置环境
```python
from apigptcloud import openai
openai.api_key = ""
openai.api_base = ""
```

## ChatCompletion
```python
res = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"}
    ],
    temperature=2,
)
```
## Completion
```python
res = openai.Completion.create(
    model="gpt-3.5-turbo",
    prompt="I am a apple, and you are",
    max_tokens=7,
    temperature=0
)
```
## Embedding
```python
res = openai.Embedding.create(
    model="gpt-3.5-turbo",
    input="The food was delicious and the waiter..."
)
```