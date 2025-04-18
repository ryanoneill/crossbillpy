"""Module that includes the `StringServer` class."""

from ..server import Server
from .pipeline_factory import StringPipelineFactory
from .request import StringRequest
from .response import StringResponse


class StringServer(Server[StringRequest, StringResponse]):
    """A server that accepts `StringRequest`s and returns `StringResponse`s."""

    def __init__(self) -> None:
        """Initialize a `StringServer`."""
        pipeline_factory = StringPipelineFactory()
        super().__init__(pipeline_factory)
