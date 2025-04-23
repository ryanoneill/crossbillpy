import pytest

from crossbill.core import Service
from crossbill.string import (
    StringEchoService,
    StringRequest,
    StringResponse,
    StringService,
)


async def test_service_base_not_implemented() -> None:
    service = Service[StringRequest, StringResponse]()
    with pytest.raises(NotImplementedError):
        _ = await service(StringRequest("hello"))


async def test_string_service_base_not_implemented() -> None:
    service = StringService()
    with pytest.raises(NotImplementedError):
        _ = await service(StringRequest("hello"))


async def test_echo() -> None:
    service = StringEchoService()
    request = StringRequest("hello")
    response = await service(request)
    result = response.value
    assert result == "hello"
