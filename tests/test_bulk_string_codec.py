from crossbill.redis import BulkStringCodec


async def test_bulk_string_codec_encode() -> None:
    codec = BulkStringCodec()
    result = await codec.encode("hello")
    assert result == b"$5\r\nhello\r\n"

async def test_bulk_string_codec_decode() -> None:
    codec = BulkStringCodec()
    result = await codec.decode(b"$5\r\nhello\r\n")
    assert result == "hello"
