from .completions import Completions

__all__ = ["Chat"]


class Chat:

    def __init__(self, client):
        self._client = client

    @property
    def completions(self):
        return Completions(self._client)
