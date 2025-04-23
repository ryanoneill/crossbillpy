import pytest

from crossbill.core import CombinedFilter, Filter, FilteredService, Service
from crossbill.string import StringEchoService, StringRequest, StringResponse


class ReverseResponseFilter(Filter[StringRequest, StringResponse]):
    async def __call__(
        self, request: StringRequest, service: Service[StringRequest, StringResponse]
    ) -> StringResponse:
        response = await service(request)
        response.value = response.value[::-1]
        return response


class UppercaseFilter(Filter[StringRequest, StringResponse]):
    async def __call__(
        self, request: StringRequest, service: Service[StringRequest, StringResponse]
    ) -> StringResponse:
        response = await service(request)
        response.value = response.value.upper()
        return response


async def test_filter_base_not_implemented() -> None:
    filter = Filter()
    request = StringRequest("test")
    service = StringEchoService()
    with pytest.raises(NotImplementedError):
        _ = await filter(request, service)


async def test_reverse_response() -> None:
    filter = ReverseResponseFilter()

    # Non-filtered
    service = StringEchoService()
    request = StringRequest("hello")
    response = await service(request)
    result = response.value
    assert result == "hello"

    # Filtered
    request = StringRequest("hello")
    filtered = FilteredService(filter, service)
    response = await filtered(request)
    result = response.value
    assert result == "olleh"


async def test_combined_filter() -> None:
    combined = CombinedFilter([UppercaseFilter(), ReverseResponseFilter()])
    request = StringRequest("hello")
    filtered = FilteredService(combined, StringEchoService())
    response = await filtered(request)
    result = response.value
    assert result == "OLLEH"
