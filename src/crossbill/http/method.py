"""Module that provides the `Method` class."""

from enum import Enum, auto


class Method(Enum):
    """Representation of an HTTP Request Method, which indicates its purpose."""

    GET = auto()
    HEAD = auto()
    POST = auto()
    PUT = auto()
    DELETE = auto()
    CONNECT = auto()
    OPTIONS = auto()
    TRACE = auto()
    PATCH = auto()

    def __str__(self) -> str:
        """Return the `Method` name as its uppercase version."""
        return f"{self.name}"
