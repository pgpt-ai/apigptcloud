# Claude API 调用方法

## 配置环境
```python
from apigptcloud import claude
claude.api_key = ""
claude.api_base = ""
```
## Completion
```python
res = claude.Completion.create(
    model="claude-1",
    prompt="I am a apple, and you are",
    max_tokens_to_sample=256
)
```