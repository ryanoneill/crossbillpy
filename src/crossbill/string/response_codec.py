"""Module that includes the `StringResponseCodec` class."""

from ..core import ResponseCodec
from .response import StringResponse


class StringResponseCodec(ResponseCodec[StringResponse]):
    """A `StringResponseCodec` converts between `bytes` and a `StringResponse`."""

    async def encode(self, data: StringResponse) -> bytes:
        """Convert from a `StringResponse` to `bytes`."""
        return data.value.encode()

    async def decode(self, data: bytes) -> StringResponse:
        """Convert from `bytes` to a `StringResponse`."""
        return StringResponse(data.decode())
