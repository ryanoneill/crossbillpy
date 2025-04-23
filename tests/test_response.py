import pytest
from strings import StringResponse, StringResponseCodec

from crossbill.bytes import BytesResponse
from crossbill.core import Response


def test_response_is_not_implemented() -> None:
    with pytest.raises(NotImplementedError):
        _ = Response()


def test_bytes_response() -> None:
    response = BytesResponse(b"12345")
    assert response.value == b"12345"


def test_string_response() -> None:
    response = StringResponse("abcdefg")
    assert response.value == "abcdefg"


async def test_response_codec() -> None:
    data = b"\xf0\x9f\xa4\xa9"  # "🤩"
    codec = StringResponseCodec()
    response = await codec.decode(data)
    assert isinstance(response, StringResponse)
    result = await codec.encode(response)
    assert result == data
