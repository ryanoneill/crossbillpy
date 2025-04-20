"""Module that includes `StringService` and `StringEchoService` classes."""

from abc import abstractmethod

from ..core import Service
from .request import StringRequest
from .response import StringResponse


class StringService(Service[StringRequest, StringResponse]):
    """A `StringService` is a `Service[StringRequest, StringResponse]`."""

    @abstractmethod
    async def __call__(self, request: StringRequest) -> StringResponse:
        """Return a `StringResponse` based on the provided `StringRequest`."""
        raise NotImplementedError()


class StringEchoService(StringService):
    """A `StringEchoService` returns the `value` of the `StringRequest`."""

    async def __call__(self, request: StringRequest) -> StringResponse:
        """Return the `value` of the `StringRequest` in a `StringResponse`."""
        return StringResponse(request.value)
