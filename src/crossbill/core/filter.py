"""Module that includes the `Filter` abstract class."""

from abc import abstractmethod
from typing import Generic

from .request import RequestType
from .response import ResponseType
from .service import Service


class Filter(Generic[RequestType, ResponseType]):
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
        pass
