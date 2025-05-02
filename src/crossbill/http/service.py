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


class HttpEchoService(HttpService):
    """An exemplary `HttpService` that returns the `body` passed by the `HttpClient`.

    This `Service` is most useful for testing and deconstructing `HttpRequest`s sent
    by non-crossbill clients.
    """

    async def __call__(self, request: HttpRequest) -> HttpResponse:
        """Return the same `body` passed by the `HttpRequest`."""
        response = HttpResponse()
        response.body = request.body
        response.headers["Content-Length"] = str(len(request.body))
        response.headers["Content-Type"] = request.headers["Content-Type"]

        return response
