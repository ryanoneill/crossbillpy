"""Module that includes the `StringResponse` class."""

from ..core import WrappedResponse


class StringResponse(WrappedResponse[str]):
    """Descendant of `Response` that contains a `str`."""
