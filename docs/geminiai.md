# GeminiAI API Usage

## Config
```python
from apigptcloud import geminiai
geminiai.api_key = ""
geminiai.api_base = ""
```
If `geminiai.api_base` is not specified, the default endpoint [gemini.pgpt.cloud](https://gemini.pgpt.cloud) will be used. Please fill in the corresponding API Key in `geminiai.api_key`.

## Chat
Request example:
```python
res = geminiai.chat.completions.create(
    model="gemini-pro",
    messages=[
        {
            "role": "user",
            "parts": [
                {
                    "text": "hi"
                },
            ]
        }
    ]
)
```
Response example:
```json
{
    "message": "Hello, this message is from apigpt.cloud! How may I assist you today?"
}
```
