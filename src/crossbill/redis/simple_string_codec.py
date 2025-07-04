"""Module that includes the `SimpleStringCodec` class."""

from io import BytesIO

from ..core import Codec


class SimpleStringCodec(Codec[str, bytes]):
    """A `SimpleStringCodec converts between simple string `bytes` and a `str`."""

    async def encode(self, data: str) -> bytes:
        """Converts from a `str` to Simple String `bytes`."""
        result = "+" + data + "\r\n"
        return result.encode()

    async def decode(self, data: bytes) -> str:
        """Converts from Simple String `bytes` to `str`."""
        reader = BytesIO(data)
        plus = reader.read(1)
        assert(plus == b"+")
        rest = reader.read()
        assert(rest[-2:] == b"\r\n")
        result = rest.decode().rstrip()

        return result
