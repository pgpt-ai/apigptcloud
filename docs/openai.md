# OpenAI API Usage

## Config
```python
from apigptcloud import openai
openai.api_key = ""
openai.api_base = ""
```

## Chat
Request example:
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
Response example:
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
Compeletion was deprecated on January 4th, 2024. Please use `gpt-3.5-turbo-instruct` model as a substitute. The usage is the same as Chat.

## Embedding
Request example:
```python
res = openai.embeddings.create(
    model="gpt-3.5-turbo",
    input="The food was delicious and the waiter..."
)
```
Response example:
```json
{
  'object': 'list', 
  'data': [{'object': 'embedding', 'index': 0, 'embedding': [...]}], 
  'model': 'ada', 
  'usage': {'prompt_tokens': 8, 'total_tokens': 8}
}
```