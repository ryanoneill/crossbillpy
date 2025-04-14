"""Module that includes the `Request` abstract class."""

from abc import abstractmethod


class Request:
    """A `Request` is the input type of a `Service`.

    A `Service` is an asynchronous function from a `Request` to a `Response`.
    Classes that derive from this abstract implementation of `Request` should
    act as the input parameter to a `Service`'s `apply` method.
    """
    @abstractmethod
    def __init__(self) -> None:
        """Initialize a Request.

        This method is abstract, so this `crossbill.core` `Request` should not
        be initialized directly. Instead a concrete `Request` type based on this
        type should be used.
        """
        pass
