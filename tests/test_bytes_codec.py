import pytest

from crossbill.bytes import (
    BytesRequest,
    BytesRequestCodec,
    BytesResponse,
    BytesResponseCodec,
)


@pytest.mark.asyncio
async def test_bytes_request_codec() -> None:
    codec = BytesRequestCodec()
    request = BytesRequest(b"hello")
    result = await codec.encode(request)
    assert result == b"hello"

    decoded = await codec.decode(result)
    assert decoded.value == b"hello"


@pytest.mark.asyncio
async def test_bytes_response_codec() -> None:
    codec = BytesResponseCodec()
    response = BytesResponse(b"goodbye")
    result = await codec.encode(response)
    assert result == b"goodbye"

    decoded = await codec.decode(result)
    assert decoded.value == b"goodbye"
