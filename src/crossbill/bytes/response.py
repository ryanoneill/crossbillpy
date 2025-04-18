"""Module that includes the `BytesResponse` class."""

from ..core import Response


class BytesResponse(Response):
    """Descendant of `Response` that contains `bytes`."""

    def __init__(self, value: bytes) -> None:
        """Create a `BytesResponse` based on the provided `bytes`."""
        self.value = value
