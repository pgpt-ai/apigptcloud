# 开发文档

## 设计思路
* 为了实现轻量化，本程序尽量使用 Python 内置库（如 requests, json)，不使用第三方库。
* 本程序所有 API 的调用方式以[completions.py](../apigptcloud/openai/chat/completions.py)为模版，其他 API 调用方式的设计思路与此类似。该文件内有详细注释可供参考。