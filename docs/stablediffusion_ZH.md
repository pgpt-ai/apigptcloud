# Stable Diffusion API 调用方法

## 配置环境

```python
from pgpt import stablediffusion

stablediffusion.api_key = ""
stablediffusion.api_base = ""
```

## 画图
请求示例：
```python
res = stablediffusion.draw.create(
    prompt="Cat", # 提示词
    quantity=1, # 生成数量
    size="16:9" # 比例：'16:9', '1:1', '9:16', '3:4', '4:3'
)
```
返回示例：
```json
{
  "urls": [
    "https://silkroadtech.png"
  ],
  "object": "draw",
  "prompt": "Cat",
  "model": "stable_diffusion_2_1",
  "created": 14,
  "end_at": 25
}
```