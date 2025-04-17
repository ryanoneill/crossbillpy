"""Module that includes the `Service` abstract class."""

from abc import abstractmethod

from .reqrep import ReqRepType
from .request import RequestType
from .response import ResponseType


class Service(ReqRepType):
    """A `Service` is an asynchronous function from a `Request` to a `Response`.

    A `Service` transforms an instance of an input type (i.e. `Request`) to an
    instance of an output type (i.e. `Response`) asynchronously. An instance of
    a `Service` can be used as an asynchronous function directly by allowing
    Python to use its `__call__` method. This method within `Service` is abstract
    and it's expected that concrete implementations of `Service` define it.
    """

    @abstractmethod
    async def __call__(self, request: RequestType) -> ResponseType:
        """Asynchronous function from `RequestType` to `ResponseType`.

        This method asynchronously returns an instance of a `ResponseType`
        based on the instance of the `RequestType` passed in. This method
        can be invoked via the `Service` object itself by using the `Service`
        object instance as a function. This particular version is abstract.
        Concrete implementations of `Service` should define it.
        """
        raise NotImplementedError()
