"""Module that includes the `BigNumberCodec` class."""
from io import BytesIO

from ..core import Codec


class BigNumberCodec(Codec[int, bytes]):
    async def encode(self, data: int) -> bytes:
        """Converts from a large `int` to big number `bytes`."""
        result = "(" + str(data) + "\r\n"
        return result.encode()

    async def decode(self, data: bytes) -> int:
        """Converts from big number `bytes` to a large `int`."""
        reader = BytesIO(data)
        paren = reader.read(1)
        assert(paren == b"(")
        rest = reader.read()
        assert(rest[-2:] == b"\r\n")
        result = rest.decode().rstrip()

        return int(result)
