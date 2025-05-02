"""Module that includes the `HttpClient` class."""

from ..client import Client
from .request import HttpRequest
from .request_codec import HttpRequestCodec
from .response import HttpResponse
from .response_codec import HttpResponseCodec


class HttpClient(Client[HttpRequest, HttpResponse]):
    """An `HttpClient` sends `HttpRequest`s and receives `HttpResponse`s."""

    def __init__(self) -> None:
        """Initialize a `HttpClient`."""
        request_codec = HttpRequestCodec()
        response_codec = HttpResponseCodec()
        super().__init__(request_codec, response_codec)
