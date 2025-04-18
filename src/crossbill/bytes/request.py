"""Module that includes the `BytesRequest` class."""

from ..core import Request


class BytesRequest(Request):
    """Descendant of `Request` that contains `bytes`."""

    def __init__(self, value: bytes) -> None:
        """Create a `BytesRequest` based on the provided `bytes`."""
        self.value = value
