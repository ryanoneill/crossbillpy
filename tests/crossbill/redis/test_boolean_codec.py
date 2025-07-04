from crossbill.redis import BooleanCodec


async def test_true_boolean_codec_encode() -> None:
    codec = BooleanCodec()
    result = await codec.encode(True)
    assert result == b"#t\r\n"

async def test_true_boolean_codec_decode() -> None:
    codec = BooleanCodec()
    result = await codec.decode(b"#t\r\n")
    assert result

async def test_false_boolean_codec_encode() -> None:
    codec = BooleanCodec()
    result = await codec.encode(False)
    assert result == b"#f\r\n"

async def test_false_boolean_codec_decode() -> None:
    codec = BooleanCodec()
    result = await codec.decode(b"#f\r\n")
    assert not result

