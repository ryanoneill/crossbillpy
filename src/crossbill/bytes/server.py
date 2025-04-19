"""Module that includes the `BytesServer` class."""

from ..server import Server
from .pipeline_factory import BytesPipelineFactory
from .request import BytesRequest
from .response import BytesResponse


class BytesServer(Server[BytesRequest, BytesResponse]):
    """A server that accepts `BytesRequest`s and returns `BytesResponse`s."""

    def __init__(self) -> None:
        """Initializes a `BytesServer`."""
        pipeline_factory = BytesPipelineFactory()
        super().__init__(pipeline_factory)
