import requests
import apigptcloud


api_key: str = ""

models = {
    "openai-chat": ['gpt-3.5-turbo', 'gpt-3.5-turbo-16k', 'gpt-4', 'gpt-4-32k', 'gpt-4-turbo', 'gpt-3.5-turbo-instruct'],
    "openai-embeddings": ['text-embedding-ada-002'],
    "claude-completions": ['claude-1'],
    "stablediffusion": ["stablediffusion"],
    "audioai-speech": ["audioai-speech"],
    "audioai-transcriptions": ["audioai-transcriptions"],
    "textai": ["textai"],

}

reverse_models = {v: k for k, values in models.items() for v in values}


def create(model: str, **kwargs):
    key = reverse_models[model]
    print("Now using "+key)
    if key == "openai-chat":
        apigptcloud.openai.api_key = api_key
        try:
            return apigptcloud.openai.chat.completions.create(model, **kwargs)
        except Exception as e:
            return apigptcloud.openai.chat.completions.create(model, **kwargs)

    elif key == "openai-embeddings":
        apigptcloud.openai.api_key = api_key
        try:
            return apigptcloud.openai.embeddings.create(model, **kwargs)
        except Exception as e:
            return apigptcloud.openai.embeddings.create(model, **kwargs)

    elif key == "claude-completions":
        apigptcloud.claude.api_key = api_key
        try:
            return apigptcloud.claude.completions.create(model, **kwargs)
        except Exception as e:
            return apigptcloud.claude.completions.create(model, **kwargs)

    elif key == "stablediffusion":
        apigptcloud.stablediffusion.api_key = api_key
        try:
            return apigptcloud.stablediffusion.draw.create(**kwargs)
        except Exception as e:
            return apigptcloud.stablediffusion.draw.create(**kwargs)

    elif key == "audioai-speech":
        apigptcloud.audioai.api_key = api_key
        try:
            return apigptcloud.audioai.speech.create(model, **kwargs)
        except Exception as e:
            return apigptcloud.audioai.speech.create(model, **kwargs)

    elif key == "audioai-transcriptions":
        apigptcloud.audioai.api_key = api_key
        try:
            return apigptcloud.audioai.transcriptions.create(model, **kwargs)
        except Exception as e:
            return apigptcloud.audioai.transcriptions.create(model, **kwargs)

    elif key == "textai":
        apigptcloud.textai.api_key = api_key
        try:
            return apigptcloud.textai.translations.create(model, **kwargs)
        except Exception as e:
            return apigptcloud.textai.translations.create(model, **kwargs)