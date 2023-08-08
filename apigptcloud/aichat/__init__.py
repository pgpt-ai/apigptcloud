from . import (
    auth,
    Embedding,
    Chat,
)

url = "http://192.168.1.19:8000"
# url = "https://pgpt.dev.freedropship.cn"
# url = 'https://app.pgpt.cloud'

global_headers = {
        'Cache-Control': "no-cache",
        'Accept': "*/*",
        'Accept-Encoding': "gzip, deflate, br",
        'Connection': "keep-alive",
}
