# Speech Usage

## Config
```python
from apigptcloud import speech
speech.api_key = ""
```

## Text to Speech
Request example:  
Voice: "zh-CN-XiaoxiaoNeural"  
Content: "你好今天天气如何?"
```python
res = speech.tts.text_2_speech("zh-CN-XiaoxiaoNeural", "你好今天天气如何?")
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
* WAV  
  Request example:  
  File name: "zh-CN_0.wav"  
  File path: "./test/zh-CN_0.wav"  
  Language: "zh-CN"  
  ```python
  res = speech.stt.speech_2_text_wav("zh-CN_0.wav", "./test/zh-CN_0.wav", "zh-CN")
  ```
  Response example:
    ```json
    {
      "text": "你好，今天天气如何？"
    }
    ```
* AMR  
  Request example:  
  File name: "en-US_0.amr"  
  File path: "./test/en-US_0.amr"  
  Language: "en-US"  
  ```python
  res = speech.stt.speech_2_text_amr("en-US_0.amr", "./test/en-US_0.amr", "en-US")
  ```
  Response example:
    ```json
    {
      "text": "Today was a beautiful day. We had a great time taking along Long walk In the morning. The county slide was in full bloom, yet the air was crisp and cold. Towards the end of the day, clouds came in forecasting much needed rain."
    }
    ```
## Get Voice List
Request example:  
```python
res = speech.tts.text_2_speech_voices()
```
Response example:
```python
[{...}, {...}, {...}]
```
