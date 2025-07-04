from crossbill.redis import NullCodec


async def test_null_codec_encode() -> None:
    codec = NullCodec()
    result = await codec.encode(None)
    assert result == b"_\r\n"

async def test_null_codec_decode() -> None:
    codec = NullCodec()
    result = await codec.decode(b"_\r\n")
    assert result is None

