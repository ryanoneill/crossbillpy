"""Module that includes the `IntegerCodec` class."""

from io import BytesIO

from ..core import Codec


class IntegerCodec(Codec[int, bytes]):
    """An `IntegerCodec` converts between integer `bytes` and an `int`."""

    async def encode(self, data: int) -> bytes:
        """Converts from an `int` to integer `bytes`."""
        result = ":" + str(data) + "\r\n"
        return result.encode()

    async def decode(self, data: bytes) -> int:
        """Converts from integer `bytes` to an `int`."""
        reader = BytesIO(data)
        colon = reader.read(1)
        assert(colon == b":")
        rest = reader.read()
        assert(rest[-2:] == b"\r\n")
        result = rest.decode().rstrip()

        return int(result)
