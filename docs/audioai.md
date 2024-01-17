# AudioAI Usage

## Config
```python
from apigptcloud import audioai
audioai.api_key = ""
```

## Text to Speech
Request example:
```python
res = audioai.speech.create(
  "model", # Model
  "zh-CN-XiaoxiaoNeural", # Voice
  "你好今天天气如何?" # Content
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
  "model", # Model
  file, # File
  "zh-CN" # Language
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
