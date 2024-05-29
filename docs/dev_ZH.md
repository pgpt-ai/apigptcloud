# 开发文档

## 设计思路
* 为了实现轻量化，本程序尽量使用 Python 内置库（如 requests, json)，不使用第三方库。
* 本程序所有 API 的调用方式以[completions.py](../pgptai/openai/chat/completions.py)为模版，其他 API 调用方式的设计思路与此类似。该文件内有详细注释可供参考。
* 所有 API 调用方式尽量与官方保持一致，如有不同，需在文档中说明。
* 每一个模块内的`__init__.py`文件中，都会声明`api_key`和`api_base`。前者是为了存储用户密钥，后者是为了存储API的基础URL，一般为 pgpt 端点。
* 新增模块时，需在[pgptai/\_\_init\_\_.py](../pgptai/__init__.py)中添加对应的模块。以便用户可以`import`该模块。