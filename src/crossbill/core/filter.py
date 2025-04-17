"""Module that includes the `Filter` abstract class."""

from abc import abstractmethod

from .reqrep import ReqRepType
from .request import RequestType
from .response import ResponseType
from .service import Service


class Filter(ReqRepType):
    """A `Filter` decorates a `Service` adding additional functionality.

    A `Filter` wraps a `Service` and allows for modification of the `Request`
    before it's passed to the `Service`, modification of the `Response` after
    it's been returned by the `Service`, or both.

    The current definition of a `Filter` does not allow for the manipulation of
    the `RequestType` or the `ResponseType` and so operates as a `SimpleFilter`.

    The API for composing `Filter`s together, or even composing `Filter`s on
    top of `Service`s has yet to be decided, and therefore the `Filter` is not
    yet usable.
    """

    @abstractmethod
    async def __call__(
        self, request: RequestType, service: Service[RequestType, ResponseType]
    ) -> ResponseType:
        """Asynchronously returns a `Response` given a `Request` and a `Service`.

        A `Filter` wraps a `Service` providing additional functionality that should
        not be contained directly within the `Service` itself. Often, this is more
        generic functionality that should or can be included for the type of `Service`
        regardless of the specifics of that `Service`'s implementation.

        The `Filter` class is abstract, and it's expected that this method is
        implemented by implementers, but this method should generally only be
        called by the library.
        """
        raise NotImplementedError
