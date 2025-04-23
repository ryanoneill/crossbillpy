import pytest

from crossbill.bytes import BytesRequest
from crossbill.core import Request
from crossbill.string import StringRequest, StringRequestCodec


def test_request_is_not_implemented() -> None:
    with pytest.raises(NotImplementedError):
        _ = Request()


def test_bytes_request() -> None:
    request = BytesRequest(b"12345")
    assert request.value == b"12345"


def test_string_request() -> None:
    request = StringRequest("abcdefg")
    assert request.value == "abcdefg"


async def test_request_codec() -> None:
    data = b"\xf0\x9f\xa4\xa9"  # "🤩"
    codec = StringRequestCodec()
    request = await codec.decode(data)
    assert isinstance(request, StringRequest)
    result = await codec.encode(request)
    assert result == data
