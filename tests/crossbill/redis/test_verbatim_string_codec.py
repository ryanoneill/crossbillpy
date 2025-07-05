from crossbill.redis import VerbatimStringCodec


async def test_verbatim_string_codec_encode() -> None:
    codec = VerbatimStringCodec()
    result = await codec.encode(("txt", "Some string"))
    assert result == b"=15\r\ntxt:Some string\r\n"

async def test_verbatim_string_codec_decode() -> None:
    codec = VerbatimStringCodec()
    result = await codec.decode(b"=15\r\ntxt:Some string\r\n")
    assert result == ("txt", "Some string")

