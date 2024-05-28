from typing import Union, Required, TypedDict, Dict

from typing_extensions import Literal


__all__ = ["ChatCompletionFunctionCallItem", "FunctionCall", "Function", "FunctionParameters"]


class ChatCompletionFunctionCallItem(TypedDict, total=False):
    name: Required[str]


FunctionCall = Union[Literal["none", "auto"], ChatCompletionFunctionCallItem]

FunctionParameters = Dict[str, object]


class Function(TypedDict, total=False):
    name: Required[str]
    """The name of the function to be called.

    Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length
    of 64.
    """

    description: str
    """
    A description of what the function does, used by the model to choose when and
    how to call the function.
    """

    parameters: FunctionParameters
    """The parameters the functions accepts, described as a JSON Schema object."""
