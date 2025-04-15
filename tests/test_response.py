import pytest

from strings import StringResponse, StringResponseCodec


@pytest.mark.anyio
async def test_response_codec() -> None:
    data = b"\xf0\x9f\xa4\xa9"  # "🤩"
    codec = StringResponseCodec()
    response = await codec.decode(data)
    assert isinstance(response, StringResponse)
    result = await codec.encode(response)
    assert result == data
