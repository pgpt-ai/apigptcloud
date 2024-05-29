class Completions:

    def __init__(self, client) -> None:
        self._client = client

    def create(self):
        raise NotImplementedError
