"""Module that provides the `ReqRepType`."""

from typing import Generic

from .request import RequestType
from .response import ResponseType

ReqRepType = Generic[RequestType, ResponseType]
