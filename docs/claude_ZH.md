# Claude API 调用方法

## 配置环境
```python
from apigptcloud import claude
claude.api_key = ""
claude.api_base = ""
```
## Completion
请求示例：
```python
res = claude.completions.create(
    model="claude-1",
    prompt="I am a apple, and you are",
    max_tokens_to_sample=256
)
```
返回示例：
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