"""Module that includes the `StringResponse` class."""

from ..core import Response


class StringResponse(Response):
    """Descendant of `Response` that contains a `str`."""

    def __init__(self, value: str) -> None:
        """Create a `StringResponse` based on the provided `str`."""
        self.value = value
