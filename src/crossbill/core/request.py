"""Module that includes the `Request` abstract class."""

from abc import abstractmethod
from typing import Generic, TypeVar

from .codec import Codec


class Request:
    """A `Request` is the input type of a `Service`.

    A `Service` is an asynchronous function from a `Request` to a `Response`.
    Classes that derive from this abstract implementation of `Request` should
    act as the input parameter to a `Service`'s `__call__` method.
    """

    @abstractmethod
    def __init__(self) -> None:
        """Initialize a Request.

        This method is abstract, so this `crossbill.core` `Request` should not
        be initialized directly. Instead a concrete `Request` type based on this
        type should be used.
        """
        raise NotImplementedError()


RequestType = TypeVar("RequestType", bound=Request)
"""A type variable based on the abstract `Request` class."""


class RequestCodec(Codec[RequestType, bytes]):
    """A `RequestCodec` transforms a `RequestType` to and from `bytes`."""


WrappedRequestType = TypeVar("WrappedRequestType")
"""A type variable used with the `WrappedRequest` class."""


class WrappedRequest(Request, Generic[WrappedRequestType]):
    """A `WrappedRequest` allows a generic type to conform to `Request`."""

    def __init__(self, value: WrappedRequestType) -> None:
        """Initialize a `WrappedRequest` based on the given `value`."""
        self.value = value
