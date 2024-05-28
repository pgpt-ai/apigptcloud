# Stable Diffusion API Usage

## Config

```python
from pgpt import stablediffusion

stablediffusion.api_key = ""
stablediffusion.api_base = ""
```

## Draw
Request example:
```python
res = stablediffusion.draw.create(
    prompt="Cat", 
    quantity=1, 
    size="16:9" #'16:9', '1:1', '9:16', '3:4', '4:3'
)
```
Response example:
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