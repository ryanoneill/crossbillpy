"""Module that includes the `NullCodec` class."""

from ..core import Codec


class NullCodec(Codec[None, bytes]):
    """A `NullCodec` converts between null `bytes` and `None`."""

    async def encode(self, data: None) -> bytes:
        """Converts from `None` to null `bytes`."""
        assert(data is None)
        return b"_\r\n"

    async def decode(self, data: bytes) -> None:
        """Converts from null `bytes` to `None`."""
        assert(data == b"_\r\n")
        return None
