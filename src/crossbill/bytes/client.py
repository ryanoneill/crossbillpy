"""Module that includes the `BytesClient` class."""

from ..client import Client
from .request import BytesRequest
from .request_codec import BytesRequestCodec
from .response import BytesResponse
from .response_codec import BytesResponseCodec


class BytesClient(Client[BytesRequest, BytesResponse]):
    """A `BytesClient` sends `BytesRequest`s and receives `BytesResponse`s."""

    def __init__(self) -> None:
        """Initialize a `BytesClient`."""
        request_codec = BytesRequestCodec()
        response_codec = BytesResponseCodec()
        super().__init__(request_codec, response_codec)
