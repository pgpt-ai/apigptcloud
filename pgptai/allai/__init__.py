from pgptai.allai import resources


BASE_ENDPOINT = 'https://ai.pgpt.cloud/'


class AllAI:
    completions: resources.Completions
    chat: resources.Chat

    def __init__(
            self,
            *,
            api_key: str | None = None,
            endpoint: str | None = BASE_ENDPOINT,
            api_version: str = 'v1'
    ):
        self.api_key = api_key
        if not endpoint:
            endpoint = BASE_ENDPOINT
        if not str(endpoint).endswith('/'):
            endpoint = endpoint + '/'
        self.endpoint = endpoint
        self.completions = resources.Completions(self)
        self.chat = resources.Chat(self)
        self.api_version = api_version


__all__ = ["AllAI"]
