"""Module that includes the `StringResponse` class."""

from ..core import WrappedResponse


class StringResponse(WrappedResponse):
    """Descendant of `Response` that contains a `str`."""
