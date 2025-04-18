"""Module that includes the `Pipeline` class."""

from .reqrep import ReqRepType
from .request import RequestCodec, RequestType
from .response import ResponseCodec, ResponseType
from .service import Service


class Pipeline(ReqRepType):
    """A `Pipeline` asynchronous takes input `bytes` and returns output `bytes`.

    A `Pipeline` follows a path of `bytes` -> `Request` -> `Service` ->
    `Response` -> `bytes`. This is done by using a `RequestCodec` to convert
    from `bytes` to a `Request`. Then the `Request` is turned into a `Response`
    by the `Service`. Next the `Response` is turned back into `bytes` by a
    `ResponseCodec` and then those `bytes` are returned by the `Pipeline`.
    """

    def __init__(
        self,
        request_codec: RequestCodec[RequestType],
        response_codec: ResponseCodec[ResponseType],
        service: Service[RequestType, ResponseType],
    ) -> None:
        """Initialize a `Pipeline` using `Codec`s and a `Service`."""
        self.request_codec = request_codec
        self.response_codec = response_codec
        self.service = service

    async def __call__(self, data: bytes) -> bytes:
        """Asynchronously return output `bytes` based on input `bytes`."""
        request = await self.request_codec.decode(data)
        response = await self.service(request)
        result = await self.response_codec.encode(response)

        return result
