"""Module that includes the `StringRequestCodec` class."""

from ..core import RequestCodec
from .request import StringRequest


class StringRequestCodec(RequestCodec[StringRequest]):
    """A `StringRequestCodec` converts between `bytes` and a `StringRequest`."""

    async def encode(self, data: StringRequest) -> bytes:
        """Convert from a `StringRequest` to `bytes`."""
        return data.value.encode()

    async def decode(self, data: bytes) -> StringRequest:
        """Convert from `bytes` to a `StringRequest`."""
        return StringRequest(data.decode())
