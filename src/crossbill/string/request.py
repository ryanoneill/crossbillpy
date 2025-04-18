"""Module that includes the `StringRequest` class."""

from ..core import Request


class StringRequest(Request):
    """Descendant of `Request` that contains a `str`."""

    def __init__(self, value: str) -> None:
        """Create a `StringRequest` based on the provided `str`."""
        self.value = value
