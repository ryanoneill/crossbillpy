import pytest

from crossbill.core import Request
from strings import StringRequest, StringRequestCodec


@pytest.mark.anyio
def test_request_is_not_implemented() -> None:
    with pytest.raises(NotImplementedError):
        _ = Request()


@pytest.mark.anyio
async def test_request_codec() -> None:
    data = b"\xf0\x9f\xa4\xa9"  # "🤩"
    codec = StringRequestCodec()
    request = await codec.decode(data)
    assert isinstance(request, StringRequest)
    result = await codec.encode(request)
    assert result == data
