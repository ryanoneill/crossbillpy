import pytest

from crossbill.http import (
    HttpEchoService,
    HttpRequest,
    HttpService,
)


async def test_http_service_base_not_implemented() -> None:
    service = HttpService()

    request = HttpRequest()

    with pytest.raises(NotImplementedError):
        _ = await service(request)


async def test_http_echo_service() -> None:
    service = HttpEchoService()

    request = HttpRequest()

    response = await service(request)
    assert response.body == b""

    message = "hello".encode()
    request = HttpRequest()
    request.headers["Content-Type"] = "text/plain"
    request.headers["Content-Length"] = str(len(message))
    request.body = message

    response = await service(request)
    assert response.body.decode() == "hello"
