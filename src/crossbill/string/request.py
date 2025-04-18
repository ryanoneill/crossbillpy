"""Module that includes the `StringRequest` class."""

from ..core import WrappedRequest


class StringRequest(WrappedRequest[str]):
    """Descendant of `Request` that contains a `str`."""
