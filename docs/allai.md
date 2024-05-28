# AllAI Usage

## Config
Please fill in the API Key of the corresponding service in `AllAI()`

```python
from pgpt import AllAI

client = AllAI(api_key='<YOUR API KEY>')
```

## Model List
Select the corresponding service by entering the name of the model, as shown below:
### OpenAI
- gpt-3.5-turbo
- gpt-3.5-turbo-16k
- gpt-4
- gpt-4-32k
- gpt-4-turbo
- gpt-4-turbo-vision
- dall-e-2
- dall-e-3

### Claude
- claude-instant-1.2
- claude-2
- claude-3

### Gemini
- gemini-pro
- gemini-pro-vision

### stabled Diffusion
- stable_diffusion

### ChatGLM
- chatglm2
- chatglm3

## Chat
Request example:

```python
from pgpt import AllAI

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
Then the function will automatically call `apigptcloud.openai.chat.completions.create()`
