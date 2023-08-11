# Stable Diffusion API 调用方法

## 配置环境
```python
from apigptcloud import stablediffusion
stablediffusion.api_key = ""
stablediffusion.api_base = ""
```

## 画图
```python
res = stablediffusion.draw.create(
    prompt="Cat", 
    quantity=1, 
    size="16:9" #'16:9', '1:1', '9:16', '3:4', '4:3'
)
```