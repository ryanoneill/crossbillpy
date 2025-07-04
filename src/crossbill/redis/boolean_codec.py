"""Module that includes the `BooleanCodec` class."""

from io import BytesIO

from ..core import Codec


class BooleanCodec(Codec[bool, bytes]):
    """A `BooleanCodec` converts between boolean `bytes` and a `bool`."""

    async def encode(self, data: bool) -> bytes:
        """Converts from a `bool` to boolean `bytes`."""
        result = "#"
        if data:
            result += "t"
        else:
            result += "f"
        result += "\r\n"
        return result.encode()

    async def decode(self, data: bytes) -> bool:
        """Converts from boolean `bytes` to a `bool`."""
        reader = BytesIO(data)
        hash = reader.read(1)
        assert(hash == b"#")
        rest = reader.read()
        assert(rest[-2:] == b"\r\n")
        value = rest[:-2]
        assert(value == b"t" or value == b"f")
        result = value == b"t"
        return result
