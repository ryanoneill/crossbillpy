"""Module that includes the `BytesPipelineFactory` class."""

from ..core import Pipeline, PipelineFactory, Service
from .request import BytesRequest
from .request_codec import BytesRequestCodec
from .response import BytesResponse
from .response_codec import BytesResponseCodec


class BytesPipelineFactory(PipelineFactory):
    """A `BytesPipelineFactory` creates a `Pipeline` based on a `Service`."""

    async def __call__(
        self, service: Service[BytesRequest, BytesResponse]
    ) -> Pipeline[BytesRequest, BytesResponse]:
        """Create a `Pipeline` based on the provided `Service`.

        A `BytesPipelineFactory` factory can create a
        `Pipeline[BytesRequest, BytesResponse]` based on the passed in
        `Service[BytesRequest, BytesResponse]`.
        """
        request_codec = BytesRequestCodec()
        response_codec = BytesResponseCodec()
        pipeline = Pipeline(request_codec, response_codec, service)
        return pipeline
