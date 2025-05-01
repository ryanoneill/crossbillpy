"""Module that includes the `HttpRequest` class."""

from collections import defaultdict
from typing import Dict

from ..core import Request
from .method import Method


class HttpRequest(Request):
    """Descendant of `Request` for use with the HTTP protocol."""

    def __init__(self) -> None:
        """Initialize an `HttpRequest`."""
        self.headers: Dict[str, str] = defaultdict(str)
        self.body: bytes = b""
        self.method: Method = Method.GET
        self.uri: str = "/"
