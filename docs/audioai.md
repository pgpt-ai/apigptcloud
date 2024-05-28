# AudioAI Usage

## Config

```python
from pgpt import audioai

audioai.api_key = ""
```

## Text to Speech
Request example:
```python
res = audioai.speech.create(
  model="model",
  voice="zh-CN-XiaoxiaoNeural",
  input="你好今天天气如何?"
)
```

Response example:
```json
{
  "text": "你好今天天气如何?", 
  "url": "https://file.wav", 
  "duration": 2.1
}
```

## Speech to Text
Request example:

```python
file = open("speech.mp3", "rb")
res = audioai.transcriptions.create(
  model="model",
  file=file,
  language="zh-CN"
)
```
Response example:
```json
{
  "text": "你好，今天天气如何？"
}
```

## Get Voice List
Request example:  
```python
res = audioai.speech.list()
```
Response example:
```python
[{...}, {...}, {...}]
```
