"""Module that includes the `HttpService` class."""

from abc import abstractmethod

from ..core import Service
from .request import HttpRequest
from .response import HttpResponse


class HttpService(Service[HttpRequest, HttpResponse]):
    """An `HttpService` is a `Service[HttpRequest, HttpResponse]`."""

    @abstractmethod
    async def __call__(self, request: HttpRequest) -> HttpResponse:
        """Return an `HttpResponse` based on the provided `HttpRequest`."""
        raise NotImplementedError()
