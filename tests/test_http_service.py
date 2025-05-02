import pytest

from crossbill.http import (
    HttpRequest,
    HttpService,
)


async def test_http_service_base_not_implemented() -> None:
    service = HttpService()

    request = HttpRequest()
    request.uri = "/"

    with pytest.raises(NotImplementedError):
        _ = await service(request)
