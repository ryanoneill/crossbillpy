"""Module that includes the `CombinedFilter` class."""

from typing import Iterable

from .filter import Filter
from .filtered_service import FilteredService
from .request import RequestType
from .response import ResponseType
from .service import Service


class CombinedFilter(Filter[RequestType, ResponseType]):
    """`CombinedFilter` fuses multiple `Filter`s together into a single `Filter`."""

    def __init__(self, filters: Iterable[Filter[RequestType, ResponseType]]) -> None:
        """Initializes a `CombinedFilter` and will apply all `Filter`s provided."""
        self.filters = list(filters)

    def _combine(
        self, service: Service[RequestType, ResponseType]
    ) -> Service[RequestType, ResponseType]:
        combined = service
        for filter in reversed(self.filters):
            combined = FilteredService(filter, combined)
        return combined

    async def __call__(
        self, request: RequestType, service: Service[RequestType, ResponseType]
    ) -> ResponseType:
        """Asynchronously returns a `Response` based on the provided arguments."""
        combined = self._combine(service)
        return await combined(request)
