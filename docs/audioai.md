# AudioAI Usage

## Config
```python
from apigptcloud import audioai
audioai.api_key = ""
```

## Text to Speech
Request example:  
Model: "model"  
Voice: "zh-CN-XiaoxiaoNeural"  
Content: "你好今天天气如何?"
```python
res = audioai.speech.create(
  "model", 
  "zh-CN-XiaoxiaoNeural", 
  "你好今天天气如何?"
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
Model: "model"    
File: "speech.mp3"  
Language: "zh-CN"
```python
file = open("speech.mp3", "rb")
res = audioai.transcriptions.create(
  "model", 
  file, 
  "zh-CN"
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
