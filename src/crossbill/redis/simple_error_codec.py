"""Module that includes the `SimpleErrorCodec` class."""

from io import BytesIO

from ..core import Codec


class SimpleErrorCodec(Codec[str, bytes]):
    """A `SimpleErrorCodec converts between simple error `bytes` and a `str`."""

    async def encode(self, data: str) -> bytes:
        """Converts from a `str` to Simple Error `bytes`."""
        result = "-" + data + "\r\n"
        return result.encode()

    async def decode(self, data: bytes) -> str:
        """Converts from Simple Error `bytes` to `str`."""
        reader = BytesIO(data)
        plus = reader.read(1)
        assert(plus == b"-")
        rest = reader.read()
        assert(rest[-2:] == b"\r\n")
        result = rest.decode().rstrip()

        return result
