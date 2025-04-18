"""Module that includes the `StringPipelineFactory` class."""

from ..core import Pipeline, PipelineFactory, Service
from .request import StringRequest
from .request_codec import StringRequestCodec
from .response import StringResponse
from .response_codec import StringResponseCodec


class StringPipelineFactory(PipelineFactory):
    """A `StringPipelineFactory` creates a `Pipeline` based on a `Service`."""

    async def __call__(
        self, service: Service[StringRequest, StringResponse]
    ) -> Pipeline[StringRequest, StringResponse]:
        """Create a `Pipeline` based on the provided `Service`.

        A `StringPipelineFactory` factory can create a
        `Pipeline[StringRequest, StringResponse]` based on the passed in
        `Service[StringRequest, StringResponse]`.
        """
        request_codec = StringRequestCodec()
        response_codec = StringResponseCodec()
        pipeline = Pipeline(request_codec, response_codec, service)
        return pipeline
