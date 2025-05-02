"""Module that includes the `HttpServer` class."""

from ..server import Server
from .pipeline_factory import HttpPipelineFactory
from .request import HttpRequest
from .response import HttpResponse


class HttpServer(Server[HttpRequest, HttpResponse]):
    """A server that accepts `HttpRequest`s and returns `HttpResponse`s."""

    def __init__(self) -> None:
        """Initialize an `HttpServer`."""
        pipeline_factory = HttpPipelineFactory()
        super().__init__(pipeline_factory)
