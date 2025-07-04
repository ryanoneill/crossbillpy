from crossbill.redis import SimpleErrorCodec


async def test_simple_error_codec_encode() -> None:
    codec = SimpleErrorCodec()
    result = await codec.encode("Error message")
    assert result == b"-Error message\r\n"

async def test_simple_string_codec_decode() -> None:
    codec = SimpleErrorCodec()
    result = await codec.decode(b"-Error message\r\n")
    assert result == "Error message"
