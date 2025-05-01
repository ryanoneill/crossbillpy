"""Module that includes the `HttpResponse` class."""

from collections import defaultdict
from typing import Dict

from ..core import Response
from .status import Status


class HttpResponse(Response):
    """Descendant of `Response` for use with the HTTP protocol."""

    def __init__(self) -> None:
        """Initialize an `HttpResponse`."""
        self.headers: Dict[str, str] = defaultdict(str)
        self.status: Status = Status.OK
        self.body: bytes = b""
