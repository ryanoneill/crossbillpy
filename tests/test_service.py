import pytest
from strings import EchoService

from crossbill.core import Service
from crossbill.string import StringRequest, StringResponse


@pytest.mark.asyncio
async def test_service_base_not_implemented() -> None:
    service = Service[StringRequest, StringResponse]()
    with pytest.raises(NotImplementedError):
        _ = await service(StringRequest("hello"))


@pytest.mark.asyncio
async def test_echo() -> None:
    service = EchoService()
    request = StringRequest("hello")
    response = await service(request)
    result = response.value
    assert result == "hello"
