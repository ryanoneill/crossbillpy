"""Module that includes the `BytesRequest` class."""

from ..core import WrappedRequest


class BytesRequest(WrappedRequest[bytes]):
    """Descendant of `Request` that contains `bytes`."""
