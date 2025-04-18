"""Module that includes the `Response` abstract class."""

from abc import abstractmethod
from typing import Generic, TypeVar

from .codec import Codec


class Response:
    """A `Response` is the output type of a `Service`.

    A `Service` is an asynchronous function from a `Request` to a `Response`.
    Classes that derive from this abstract implementation of `Response` should
    act as the output parameter for a `Service`'s `__call__` method.
    """

    @abstractmethod
    def __init__(self) -> None:
        """Initialize a Response.

        This method is abstract, so this `crossbill.core` `Response` should not
        be initialized directly. Instead a concrete `Response` type based on this
        type should be used.
        """
        raise NotImplementedError()


ResponseType = TypeVar("ResponseType", bound=Response)
"""A type variable based on the abstract `Response` class."""


class ResponseCodec(Codec[ResponseType, bytes]):
    """A `ResponseCodec` transforms a `ResponseType` to and from `bytes`."""


WrappedResponseType = TypeVar("WrappedResponseType")
"""A type variable used with the `WrappedResponse` class."""


class WrappedResponse(Response, Generic[WrappedResponseType]):
    """A `WrappedResponse` allows a generic type to conform to `Response`."""

    def __init__(self, value: WrappedResponseType) -> None:
        """Initialize a `WrappedResponse` based on the given `value`."""
        self.value = value
