# Speech 调用方法

## 配置环境

```python
from apigptcloud import audioai
audioai.api_key = ""
```

## 文字转语音
请求示例：  
模型："model"  
声音："zh-CN-XiaoxiaoNeural"  
内容："你好今天天气如何?"
```python
res = audioai.speech.create(
  "model", 
  "zh-CN-XiaoxiaoNeural", 
  "你好今天天气如何?"
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
模型："model"  
文件："speech.mp3"  
语言："zh-CN"
```python
file = open("speech.mp3", "rb")
res = audioai.transcriptions.create(
  "model", 
  file, 
  "zh-CN"
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
