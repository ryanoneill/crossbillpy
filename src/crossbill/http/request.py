"""Module that includes the `HttpRequest` class."""

from collections import defaultdict

from ..core import Request
from .method import Method


class HttpRequest(Request):
    """Descendant of `Request` for use with the HTTP protocol."""

    def __init__(self) -> None:
        """Initialize an `HttpRequest`."""
        self.headers = defaultdict(str)
        self.body = b""
        self.method = Method.GET
        self.uri = "/"
