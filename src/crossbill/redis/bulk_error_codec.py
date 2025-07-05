"""Module that includes the `BulkErrorCodec` class."""

from io import BytesIO

from ..core import Codec


class BulkErrorCodec(Codec[str, bytes]):
    """A `BulkErrorCodec converts between bulk error `bytes` and a `str`."""

    async def encode(self, data: str) -> bytes:
        """Converts from a `str` to bulk error `bytes`."""
        n = len(data)
        result = "!" + str(n) + "\r\n" + data + "\r\n"
        return result.encode()

    async def decode(self, data: bytes) -> str:
        """Converts from bulk error `bytes` to `str`."""
        reader = BytesIO(data)
        bang = reader.read(1)
        assert(bang == b"!")
        length = await self._readline(reader, max_size=11)
        assert(length[-2:] == b"\r\n")
        length = int(length[:-2].decode())
        result = reader.read(length).decode()
        remaining = reader.read(2)
        assert(remaining == b"\r\n")

        return result

    # TODO: Move outside of `BulkErrorCodec`
    async def _readline(self, reader: BytesIO, max_size: int) -> bytes:
        remaining = max_size
        result = b""

        while result[-2:] != b"\r\n" and remaining > 0 and reader.readable():
            result += reader.read(1)
            remaining -= 1

        return result

