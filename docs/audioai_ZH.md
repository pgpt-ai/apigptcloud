# AudioAI 调用方法

## 配置环境

```python
from pgptai import audioai

audioai.api_key = ""
```

## 文字转语音
请求示例：  
```python
res = audioai.speech.create(
  model="model",
  voice="zh-CN-XiaoxiaoNeural",
  input="你好今天天气如何?"
)
```

返回示例：
```json
{
  "text": "你好今天天气如何?", 
  "url": "https://file.wav", 
  "duration": 2.1
}
```

## 语音转文字
请求示例：

```python
file = open("speech.mp3", "rb")
res = audioai.transcriptions.create(
    model="model",
    file=file,
    language="zh-CN"
)
```
返回示例：
```json
{
  "text": "你好，今天天气如何？"
}
```

## 获取声音列表
请求示例：
```python
res = audioai.speech.list()
```
返回示例：
```python
[{...}, {...}, {...}]
```
