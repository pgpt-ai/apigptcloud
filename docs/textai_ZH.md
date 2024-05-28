# TextAI 调用方法

## 配置环境

```python
from pgpt import textai

textai.api_key = ""
```

## 翻译
请求示例：
```python
res = textai.translations.create(
    ['zh-Hans', 'pt', 'en'],
    "下表列出了国际语音字母 (IPA) 音素、扩展语音评估方法语音字母 (X-SAMPA) 符号以及亚马逊 Polly 支持的巴西葡萄牙语语音的相应变量。"
)
```