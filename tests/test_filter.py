import pytest

from crossbill.core import Filter, Service

from strings import StringRequest, StringResponse, EchoService


class ReverseResponseFilter(Filter[StringRequest, StringResponse]):
    async def __call__(
        self, request: StringRequest, service: Service[StringRequest, StringResponse]
    ) -> StringResponse:
        response = await service(request)
        response.value = response.value[::-1]
        return response


@pytest.mark.anyio
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
