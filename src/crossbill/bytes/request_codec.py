"""Module that includes the `BytesRequestCodec` class."""

from ..core import RequestCodec
from .request import BytesRequest


class BytesRequestCodec(RequestCodec[BytesRequest]):
    """A `BytesRequestCodec` converts between `bytes` and a `BytesRequest`."""

    async def encode(self, data: BytesRequest) -> bytes:
        """Convert from a `BytesRequest` to `bytes`."""
        return data.value

    async def decode(self, data: bytes) -> BytesRequest:
        """Convert from `bytes` to a `BytesRequest`."""
        return BytesRequest(data)
