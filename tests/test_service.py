import pytest

from strings import StringRequest, EchoService

@pytest.mark.anyio
async def test_echo():
    service = EchoService()
    request = StringRequest("hello")
    response = await service(request)
    result = response.value
    assert result == "hello"
