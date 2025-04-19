"""Module that includes a `FilteredService`."""

from .filter import Filter
from .request import RequestType
from .response import ResponseType
from .service import Service


class FilteredService(Service[RequestType, ResponseType]):
    """A `FilteredService` takes a `Filter` and combines it onto a `Service`."""

    def __init__(
        self,
        filter: Filter[RequestType, ResponseType],
        service: Service[RequestType, ResponseType],
    ) -> None:
        """Initializes the `FilteredService` based on a `Filter` and a `Service`."""
        self.filter = filter
        self.service = service
        super().__init__()

    async def __call__(self, request: RequestType) -> ResponseType:
        """Asynchronously call through the `Filter` and `Service`."""
        return await self.filter(request, self.service)
