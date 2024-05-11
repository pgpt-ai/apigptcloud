import json

from typing import Iterable

from apigptcloud.allai.types.chat import chat_completions as chat_type, function_call as call_type
from apigptcloud.allai._models import CHAT_MODELS
import apigptcloud


__all__ = ['Completions']

from apigptcloud.allai.utils.functions import extract_image_generation_keywords, generate_image_prompt


class Completions:

    def __init__(self, client) -> None:
        self._client = client

    def create(self,
               *,
               model: str,
               messages: chat_type.ChatCompletionsMessagesModel,
               stream: bool = False,
               max_tokens: int = 1000,
               function_call: call_type.FunctionCall | None = 'auto',
               functions: Iterable[call_type.Function] | None = None,
               **kwargs
               ):
        error_res = chat_type.ChatCompletionsErrorResponseModel(
            status=404, error={"code": "NotFound", "message": "Model not found"}, msg='failed'
        )
        provider = CHAT_MODELS.get(model, None)
        if not provider:
            return error_res
        if provider == 'openai':
            if stream:
                return self._openai_chat_stream(
                    model=model, messages=messages, function_call=function_call, functions=functions
                )
            return self._openai_chat(
                model=model, messages=messages, function_call=function_call, functions=functions
            )
        if provider == 'claude':
            if stream:
                return self._claude_chat_stream(
                    model=model, messages=messages, function_call=function_call, functions=functions,
                    max_tokens=max_tokens
                )
            return self._claude_chat(
                model=model, messages=messages, function_call=function_call, functions=functions,
                max_tokens=max_tokens
            )
        if provider == 'sd':
            return self._stable_diffusion(messages)
        if provider == 'chatglm':
            return self._chatglm(model=model, messages=messages, max_tokens=max_tokens)
        if provider == 'gemini':
            if stream:
                return self._gemini_chat_stream(model=model, messages=messages, max_tokens=max_tokens)
            return self._gemini_chat(model=model, messages=messages, max_tokens=max_tokens)
        return error_res

    def _openai_chat(self, model, messages, function_call, functions):
        if 'dall' in model or 'ultra' in model:
            return self._dall_e_chat(model, messages)
        succeed_res = chat_type.ChatCompletionsSucceedResponseModel(
            status=200, data={}, msg='succeed'
        )
        error_res = chat_type.ChatCompletionsErrorResponseModel(
            status=500, error={}, msg='failed'
        )
        apigptcloud.openai.api_key = self._client.api_key
        if self._client.endpoint:
            base_url = f'{self._client.endpoint}{self._client.api_version}'
            apigptcloud.openai.api_base = base_url

        response = apigptcloud.openai.chat.completions.create(
            model=model,
            messages=messages,
            stream=False,
            function_call=function_call,
            functions=functions
        )
        if response.get('error'):
            error_res['error'] = response.get('error')
            return error_res
        if not response.get('choices'):
            error_res['status'] = 400
            error_res['error'] = {"code": "NoResponse", "message": "No messages Response"}
            return error_res
        succeed_res['data']['model'] = model
        succeed_res['data']['model_type'] = 'chat.completions'
        res_message = response["choices"][0]["message"]
        succeed_res['data']['response'] = {"text": res_message["content"]}
        if res_message.get('function_call'):
            succeed_res['data']['response']['function_call'] = res_message['function_call']
        return succeed_res

    def _openai_chat_stream(self, model, messages, function_call, functions):
        if 'dall' in model or 'ultra' in model:
            return json.dumps(self._dall_e_chat(model, messages))
        succeed_res = chat_type.ChatCompletionsSucceedResponseModel(
            status=200, data={}, msg='succeed'
        )
        error_res = chat_type.ChatCompletionsErrorResponseModel(
            status=500, error={}, msg='failed'
        )
        apigptcloud.openai.api_key = self._client.api_key
        if self._client.endpoint:
            base_url = f'{self._client.endpoint}{self._client.api_version}'
            apigptcloud.openai.api_base = base_url
        response = apigptcloud.openai.chat.completions.create(
            model=model,
            messages=messages,
            stream=True,
            function_call=function_call,
            functions=functions
        )
        for chunk in response:
            chunk = json.loads(chunk)
            try:
                res_message = chunk["choices"][0] if chunk["choices"] else None
                res_message = res_message["delta"] if res_message else {}
                succeed_res['data']['model'] = model
                succeed_res['data']['model_type'] = 'chat.completions.chunk'
                succeed_res['data']['response'] = {"text": res_message.get('content')}
                if res_message.get('function_call'):
                    succeed_res['data']['response']['function_call'] = res_message['function_call']
                yield json.dumps(succeed_res)
            except Exception as e:
                error_res["error"] = {"code": "ServerError", "message": str(e)}
                return json.dumps(error_res)
        return json.dumps(succeed_res)

    def _dall_e_chat(self, model, messages):
        succeed_res = chat_type.ChatCompletionsSucceedResponseModel(
            status=200, data={}, msg='succeed'
        )
        error_res = chat_type.ChatCompletionsErrorResponseModel(
            status=500, error={}, msg='failed'
        )
        apigptcloud.openai.api_key = self._client.api_key
        if self._client.endpoint:
            base_url = f'{self._client.endpoint}{self._client.api_version}'
            apigptcloud.openai.api_base = base_url
        dall_model = model
        prompt = ''
        content = messages[-1].get('content', '')
        if isinstance(content, str):
            prompt = content
        elif isinstance(content, list):
            for item in content:
                if item.get('type') == 'text':
                    prompt = item.get('text', '')
        if 'ultra' in model:
            response = apigptcloud.openai.chat.completions.create(
                model=model.replace('ultra', 'turbo'),
                messages=messages,
                stream=False,
                function_call='auto',
                functions=[extract_image_generation_keywords()]
            )
            if response.get('error'):
                error_res['error'] = response.get('error')
                return error_res
            if not response.get('choices'):
                error_res['status'] = 400
                error_res['error'] = {"code": "NoResponse", "message": "No messages Response"}
                return error_res
            res_message = response["choices"][0]["message"]
            if response.get('content'):
                succeed_res['data']['model'] = model
                succeed_res['data']['model_type'] = 'chat.completions'
                succeed_res['data']['response'] = {"text": res_message["content"]}
                return succeed_res
            res_function_call = res_message.get('function_call')
            if res_function_call:
                arguments = res_function_call.get('arguments')
                arguments = json.loads(arguments)
                prompt = generate_image_prompt(arguments, prompt)
                dall_model = 'dall-e-3'

        response = apigptcloud.openai.images.create(
            model=dall_model,
            prompt=prompt
        )
        if response.get('data'):
            succeed_res['data']['response'] = {
                'text': 'Based on your description, the following image is generated for you.',
                "images": response.get('data', [])
            }
            return succeed_res
        if response.get('error'):
            error_res['error'] = response.get('error')
            return error_res
        return error_res

    def _claude_chat(self, model, messages, function_call, functions, max_tokens):
        succeed_res = chat_type.ChatCompletionsSucceedResponseModel(
            status=200, data={}, msg='succeed'
        )
        error_res = chat_type.ChatCompletionsErrorResponseModel(
            status=500, error={}, msg='failed'
        )
        apigptcloud.claude.api_key = self._client.api_key
        if self._client.endpoint:
            base_url = f'{self._client.endpoint}claude/{self._client.api_version}'
            apigptcloud.claude.api_base = base_url
        response = apigptcloud.claude.messages.create(
            model=model,
            messages=messages,
            stream=False,
            max_tokens=max_tokens
        )
        if response.get('error'):
            error_res["error"] = response.get("error")
            return error_res
        succeed_res['data']['model'] = model
        succeed_res['data']['model_type'] = 'chat.completions'
        succeed_res['data']['response'] = {"text":  response["content"][-1]["text"]}
        return succeed_res

    def _claude_chat_stream(self, model, messages, function_call, functions, max_tokens):
        succeed_res = chat_type.ChatCompletionsSucceedResponseModel(
            status=200, data={}, msg='succeed'
        )
        error_res = chat_type.ChatCompletionsErrorResponseModel(
            status=500, error={}, msg='failed'
        )
        apigptcloud.claude.api_key = self._client.api_key
        if self._client.endpoint:
            base_url = f'{self._client.endpoint}claude/{self._client.api_version}'
            apigptcloud.claude.api_base = base_url
        response = apigptcloud.claude.messages.create(
            model=model,
            messages=messages,
            stream=True,
            max_tokens=max_tokens
        )
        for chunk in response:
            try:
                if "data: " in chunk:
                    data = json.loads(chunk.split("data: ")[-1])
                    delta = data.get('delta', {})
                    succeed_res['data'] = {
                        "model_type": "chat.completions.chunk",
                        "model": model,
                        "response": {
                            "text": delta.get('text', '')
                        }
                    }
                    yield json.dumps(succeed_res)
            except Exception as e:
                error_res["error"] = {"code":  "ServerError", "message": str(e)}
                return json.dumps(error_res)
        return json.dumps(succeed_res)

    def _stable_diffusion(self, messages, height=1024, width=1024):
        content = messages[-1].get('content', '')
        if self._client.endpoint:
            base_url = f'{self._client.endpoint}sd/{self._client.api_version}'
            apigptcloud.stablediffusion.api_base = base_url
        prompt = ''
        if isinstance(content, str):
            prompt = content
        elif isinstance(content, list):
            for item in content:
                if item.get('type') == 'text':
                    prompt = item.get('text')
        apigptcloud.stablediffusion.api_key = self._client.api_key
        succeed_res = chat_type.ChatCompletionsSucceedResponseModel(
            status=200, data={}, msg='succeed'
        )
        error_res = chat_type.ChatCompletionsErrorResponseModel(
            status=500, error={}, msg='failed'
        )
        res = apigptcloud.stablediffusion.draw.create(
            prompt=prompt,
            height=height,
            width=width
        )
        if res.get('error'):
            error_res['error'] = res.get('error')
            return error_res
        succeed_res["data"] = res
        return succeed_res

    def _chatglm(self, model, messages, max_tokens):
        succeed_res = chat_type.ChatCompletionsSucceedResponseModel(
            status=200, data={}, msg='succeed'
        )
        error_res = chat_type.ChatCompletionsErrorResponseModel(
            status=500, error={}, msg='failed'
        )
        if self._client.endpoint:
            base_url = f'{self._client.endpoint}{self._client.api_version}/chatglm'
            apigptcloud.chatglm.api_base = base_url
        res = apigptcloud.chatglm.completions.create(
            model=model,
            messages=messages,
            max_tokens=max_tokens
        )
        print('=====', res)
        if res.get('error'):
            error_res['error'] = res.get('error')
            return error_res
        choices = res.get('choices', [])
        if not choices:
            error_res['status'] = 400
            error_res['error'] = {"code": "NoResponse", "message": "No choices Response"}
            return error_res
        msg_data = choices[0].get('messages')
        if not msg_data:
            error_res['status'] = 400
            error_res['error'] = {"code": "NoResponse", "message": "No messages Response"}
            return error_res
        text = msg_data.get('content', '')
        succeed_res["data"]["response"] = {"text": text}
        return succeed_res

    def _gemini_chat(self, model, messages, max_tokens):
        from apigptcloud.allai.utils import gemini_format
        succeed_res = chat_type.ChatCompletionsSucceedResponseModel(
            status=200, data={}, msg='succeed'
        )
        error_res = chat_type.ChatCompletionsErrorResponseModel(
            status=500, error={}, msg='failed'
        )
        if self._client.endpoint:
            base_url = f'{self._client.endpoint}gemini/{self._client.api_version}'
            apigptcloud.geminiai.api_base = base_url
        apigptcloud.geminiai.api_key = self._client.api_key
        contents = gemini_format.convert_contents(messages)
        res = apigptcloud.geminiai.chat.completions.create(
            model=model,
            contents=contents,
            max_output_tokens=max_tokens
        )
        if res.get('error'):
            error_res['status'] = 400
            error_res['error'] = res.get('error')
            return error_res
        if res.get('message'):
            succeed_res['data']['model_type'] = 'chat.completions'
            succeed_res["data"]["response"] = {"text": res.get('message')}
            return succeed_res
        return error_res

    def _gemini_chat_stream(self, model, messages, max_tokens):
        from apigptcloud.allai.utils import gemini_format
        succeed_res = chat_type.ChatCompletionsSucceedResponseModel(
            status=200, data={}, msg='succeed'
        )
        error_res = chat_type.ChatCompletionsErrorResponseModel(
            status=500, error={}, msg='failed'
        )
        if self._client.endpoint:
            base_url = f'{self._client.endpoint}gemini/{self._client.api_version}'
            apigptcloud.geminiai.api_base = base_url
        apigptcloud.geminiai.api_key = self._client.api_key
        contents = gemini_format.convert_contents(messages)
        response = apigptcloud.geminiai.chat.completions.create(
            model=model,
            contents=contents,
            max_output_tokens=max_tokens,
            stream=True
        )
        for chunk in response:
            try:
                data = json.loads(chunk)
                if data.get('error'):
                    error_res["error"] = data['error']
                    yield json.dumps(error_res)
                succeed_res['data'] = {
                    "model_type": "chat.completions.chunk",
                    "model": model,
                    "response": {
                        "text": data.get('message', '')
                    }
                }
                yield json.dumps(succeed_res)
            except Exception as e:
                error_res["error"] = {"code":  "ServerError", "message": str(e)}
                yield json.dumps(error_res)
        return error_res
