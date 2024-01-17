# Speech 调用方法

## 配置环境

```python
from apigptcloud import audioai

audioai.api_key = ""
```

## 文字转语音
请求示例：  
声音："zh-CN-XiaoxiaoNeural"  
内容："你好今天天气如何?"
```python
res = speech.tts.text_2_speech("zh-CN-XiaoxiaoNeural", "你好今天天气如何?")
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
* WAV  
  请求示例：  
  文件名："zh-CN_0.wav"  
  文件路径："./test/zh-CN_0.wav"  
  语言："zh-CN"
  ```python
  res = speech.stt.create_wav("zh-CN_0.wav", "./test/zh-CN_0.wav", "zh-CN")
  ```
  返回示例：
    ```json
    {
      "text": "你好，今天天气如何？"
    }
    ```
* AMR  
  请求示例：  
  文件名："en-US_0.amr"  
  文件路径："./test/en-US_0.amr"  
  语言："en-US"  
  ```python
  res = speech.stt.speech_2_text_amr("en-US_0.amr", "./test/en-US_0.amr", "en-US")
  ```
  返回示例：
    ```json
    {
      "text": "Today was a beautiful day. We had a great time taking along Long walk In the morning. The county slide was in full bloom, yet the air was crisp and cold. Towards the end of the day, clouds came in forecasting much needed rain."
    }
    ```
## 获取声音列表
请求示例：
```python
res = speech.tts.text_2_speech_voices()
```
返回示例：
```python
[{...}, {...}, {...}]
```
