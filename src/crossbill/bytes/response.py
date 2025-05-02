"""Module that includes the `BytesResponse` class."""

from ..core import WrappedResponse


class BytesResponse(WrappedResponse[bytes]):
    """Descendant of `Response` that contains `bytes`."""
