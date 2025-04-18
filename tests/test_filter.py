import pytest

from crossbill.core import Filter, Service
from crossbill.string import StringRequest, StringResponse

from strings import EchoService


class ReverseResponseFilter(Filter[StringRequest, StringResponse]):
    async def __call__(
        self, request: StringRequest, service: Service[StringRequest, StringResponse]
    ) -> StringResponse:
        response = await service(request)
        response.value = response.value[::-1]
        return response


@pytest.mark.asyncio
async def test_filter_base_not_implemented() -> None:
    filter = Filter()
    request = StringRequest("test")
    service = EchoService()
    with pytest.raises(NotImplementedError):
        _ = await filter(request, service)


@pytest.mark.asyncio
async def test_reverse_response() -> None:
    filter = ReverseResponseFilter()

    # Non-filtered
    service = EchoService()
    request = StringRequest("hello")
    response = await service(request)
    result = response.value
    assert result == "hello"

    # Filtered
    request = StringRequest("hello")
    response = await filter(request, service)
    result = response.value
    assert result == "olleh"
