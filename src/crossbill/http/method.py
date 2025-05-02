"""Module that provides the `HttpMethod` class."""

from enum import StrEnum


class HttpMethod(StrEnum):
    """Representation of an HTTP Request Method, which indicates its purpose."""

    GET = "GET"
    HEAD = "HEAD"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    CONNECT = "CONNECT"
    OPTIONS = "OPTIONS"
    TRACE = "TRACE"
    PATCH = "PATCH"

    @property
    def verb(self) -> str:
        """Returns the uppercase version of the HTTP method name."""
        return self.value
