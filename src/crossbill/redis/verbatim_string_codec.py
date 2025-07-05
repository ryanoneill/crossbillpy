"""Module that includes the `VerbatimStringCodec` class."""

from io import BytesIO
from typing import Tuple

from ..core import Codec


class VerbatimStringCodec(Codec[Tuple[str, str], bytes]):
    """A `VerbatimStringCodec` converts between `bytes` and a `str` with encoding."""

    async def encode(self, data: Tuple[str, str]) -> bytes:
        """Converts from a `str` with encoding to `bytes`."""
        encoding, value_data = data
        assert(len(encoding) == 3)
        full = encoding + ":" + value_data
        n = len(full)
        result = "=" + str(n) + "\r\n" + full + "\r\n"

        return result.encode()

    async def decode(self, data: bytes) -> Tuple[str, str]:
        """Converts from `bytes` to a `str` with encoding."""
        reader = BytesIO(data)
        equal = reader.read(1)
        assert(equal == b"=")
        length = await self._readline(reader, max_size=11)
        assert(length[-2:] == b"\r\n")
        length = int(length[:-2].decode())
        result = reader.read(length).decode()
        remaining = reader.read(2)
        assert(remaining == b"\r\n")

        encoding, value_data = result.split(":")
        return (encoding, value_data)


    # TODO: Move outside of `VerbatimStringCodec`
    async def _readline(self, reader: BytesIO, max_size: int) -> bytes:
        remaining = max_size
        result = b""

        while result[-2:] != b"\r\n" and remaining > 0 and reader.readable():
            result += reader.read(1)
            remaining -= 1

        return result

