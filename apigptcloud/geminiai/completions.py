from .chat import completions


def create(model, contents, stream=False, **kwargs):
    return completions.create(model, contents, stream=stream, **kwargs)
