"""Module that includes the `HttpPipelineFactory` class."""

from ..core import Pipeline, PipelineFactory, Service
from .request import HttpRequest
from .request_codec import HttpRequestCodec
from .response import HttpResponse
from .response_codec import HttpResponseCodec


class HttpPipelineFactory(PipelineFactory[HttpRequest, HttpResponse]):
    """An `HttpPipelineFactory` creates a `Pipeline` based on a `Service`."""

    async def __call__(self, service: Service[HttpRequest, HttpResponse]) -> Pipeline[HttpRequest, HttpResponse]:
        """Create a `Pipeline` based on the provided `Service`.

        An `HttpPipelineFactory` factory can create a
        `Pipeline[HttpRequest, HttpResponse]` based on the passed in
        `Service[HttpRequest, HttpResponse]`.
        """
        request_codec = HttpRequestCodec()
        response_codec = HttpResponseCodec()
        pipeline = Pipeline(request_codec, response_codec, service)
        return pipeline

