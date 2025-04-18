"""Module that includes the `StringClient` class."""

from ..client import Client
from .request import StringRequest
from .request_codec import StringRequestCodec
from .response import StringResponse
from .response_codec import StringResponseCodec


class StringClient(Client[StringRequest, StringResponse]):
    """A `StringClient` sends `StringRequest`s and receives `StringResponse`s."""

    def __init__(self) -> None:
        """Initialize a `StringClient`."""
        request_codec = StringRequestCodec()
        response_codec = StringResponseCodec()
        super().__init__(request_codec, response_codec)
