# Claude API Usage

## Config
```python
from apigptcloud import claude
claude.api_key = ""
claude.api_base = ""
```
If `claude.api_base` is empty, the default endpoint [pgpt.cloud](https://pgpt.cloud) will be used. Please fill in the corresponding API Key in `claude.api_key`.

## Completion
Request example:
```python
res = claude.completions.create(
    model="claude-1",
    prompt="I am a apple, and you are",
    max_tokens_to_sample=256
)
```
Response example:
```json
{
    "completion": " Hello! My name is Claude.",
    "stop_reason": "max_tokens",
    "model": "claude-1.3",
    "truncated": false,
    "stop": null,
    "log_id": "9ea492fc390f823c1920501228dc5b483da8428adf5ddb084cb695eb2562009e",
    "exception": null
}
```