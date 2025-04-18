import pytest
from crossbill.bytes import BytesRequest, BytesRequestCodec


@pytest.mark.asyncio
async def test_bytes_request_codec() -> None:
    codec = BytesRequestCodec()
    request = BytesRequest(b"hello")
    result = await codec.encode(request)
    assert result == b"hello"

    response = await codec.decode(result)
    assert response.value == b"hello"
