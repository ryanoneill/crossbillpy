"""Module that includes the `Response` abstract class."""

from abc import abstractmethod
from typing import TypeVar


class Response:
    """A `Response` is the output type of a `Service`.

    A `Service` is an asynchronous function from a `Request` to a `Response`.
    Classes that derive from this abstract implementation of `Response` should
    act as the output parameter for a `Service`'s `apply` method.
    """
    @abstractmethod
    def __init__(self) -> None:
        """Initialize a Response.

        This method is abstract, so this `crossbill.core` `Response` should not
        be initialized directly. Instead a concrete `Response` type based on this
        type should be used.
        """
        pass

ResponseType = TypeVar('ResponseType', bound=Response)
"""A type variable based on the abstract `Response` class."""
