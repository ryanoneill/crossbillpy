"""Module that includes the `BytesResponseCodec` class."""

from ..core import ResponseCodec
from .response import BytesResponse


class BytesResponseCodec(ResponseCodec[BytesResponse]):
    """A `BytesResponseCodec` converts between `bytes` and a `BytesResponse`."""

    async def encode(self, data: BytesResponse) -> bytes:
        """Convert from a `BytesResponse` to `bytes`."""
        return data.value

    async def decode(self, data: bytes) -> BytesResponse:
        """Convert from `bytes` to a `BytesResponse`."""
        return BytesResponse(data)
