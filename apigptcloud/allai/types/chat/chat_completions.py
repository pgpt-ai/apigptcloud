from typing import TypedDict, Optional, List, Union
from typing_extensions import Literal


__all__ = ['ChatCompletionsTextContent', 'ChatCompletionsMessage', 'ChatCompletionsMessagesModel',
           'ChatCompletionsResDataModel']


class ChatCompletionsTextContent(TypedDict):
    type: Literal['text']
    text: Optional[str]


class ChatCompletionsImageContent(TypedDict):
    type: Literal['image']
    image: Optional[str]


class ChatCompletionsMessage(TypedDict):
    role: str
    content: Union[str, List[ChatCompletionsTextContent | ChatCompletionsImageContent]]


ChatCompletionsMessagesModel = List[ChatCompletionsMessage]


class ChatCompletionsResDataModel(TypedDict):
    model: str
    model_type: Optional[str]
    response: dict


class ChatCompletionsSucceedResponseModel(TypedDict):
    status: int
    data: Optional[ChatCompletionsResDataModel] | dict
    msg: str


class ChatCompletionsErrorResponseModel(TypedDict):
    status: int
    error: Optional[TypedDict("Error", {"code": str, "message": str})]
    msg: str
