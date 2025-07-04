"""Module that includes the `DoubleCodec` class."""

from io import BytesIO

from ..core import Codec


class DoubleCodec(Codec[float, bytes]):
    """A `DoubleCodec` converts between double `bytes` and a `float`."""

    async def encode(self, data: float) -> bytes:
        """Converts from a `float` to double `bytes`."""
        result = "," + str(data) + "\r\n"
        return result.encode()

    async def decode(self, data: bytes) -> float:
        """Converts from double `bytes` to a `float`."""
        reader = BytesIO(data)
        comma = reader.read(1)
        assert(comma == b",")
        rest = reader.read()
        assert(rest[-2:] == b"\r\n")
        result = rest.decode().rstrip()

        return float(result)
