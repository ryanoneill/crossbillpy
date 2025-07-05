from crossbill.redis import BigNumberCodec


async def test_big_number_codec_encode() -> None:
    codec = BigNumberCodec()
    result = await codec.encode(3492890328409238509324850943850943825024385)
    assert result == b"(3492890328409238509324850943850943825024385\r\n"

async def test_big_number_codec_decode() -> None:
    codec = BigNumberCodec()
    result = await codec.decode(b"(3492890328409238509324850943850943825024385\r\n")
    assert result == 3492890328409238509324850943850943825024385
