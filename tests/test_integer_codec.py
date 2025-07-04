from crossbill.redis import IntegerCodec


async def test_pos_integer_codec_encode() -> None:
    codec = IntegerCodec()
    result = await codec.encode(1234)
    assert result == b":1234\r\n"

async def test_neg_integer_codec_encode() -> None:
    codec = IntegerCodec()
    result = await codec.encode(-95432)
    assert result == b":-95432\r\n"

async def test_zero_integer_codec_encode() -> None:
    codec = IntegerCodec()
    result = await codec.encode(0)
    assert result == b":0\r\n"

async def test_pos_integer_codec_decode() -> None:
    codec = IntegerCodec()
    result = await codec.decode(b":1234\r\n")
    assert result == 1234
    result = await codec.decode(b":+34567\r\n")
    assert result == 34567

async def test_neg_integer_codec_decode() -> None:
    codec = IntegerCodec()
    result = await codec.decode(b":-912356\r\n")
    assert result == -912356

async def test_zero_integer_codec_decode() -> None:
    codec = IntegerCodec()
    result = await codec.decode(b":0\r\n")
    assert result == 0





