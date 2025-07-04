from crossbill.redis import SimpleStringCodec


async def test_simple_string_codec_encode() -> None:
    codec = SimpleStringCodec()
    result = await codec.encode("OK")
    assert result == b"+OK\r\n"

async def test_simple_string_codec_decode() -> None:
    codec = SimpleStringCodec()
    result = await codec.decode(b"+OK\r\n")
    assert result == "OK"
