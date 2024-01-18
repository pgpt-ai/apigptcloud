# AllAI Usage

## Config
Please fill in the API Key of the corresponding service in `allai.api_key`
```python
from apigptcloud import allai
allai.api_key = ""
```

## Model List
Select the corresponding service by entering the name of the model, as shown below:
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
Request example:
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
Then the function will automatically call `apigptcloud.openai.chat.completions.create()`