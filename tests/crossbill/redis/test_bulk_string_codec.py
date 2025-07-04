from crossbill.redis import BulkStringCodec


async def test_bulk_string_codec_encode() -> None:
    codec = BulkStringCodec()
    result = await codec.encode("hello")
    assert result == b"$5\r\nhello\r\n"

async def test_bulk_string_codec_decode() -> None:
    codec = BulkStringCodec()
    result = await codec.decode(b"$5\r\nhello\r\n")
    assert result == "hello"

async def test_empty_bulk_string_codec_encode() -> None:
    codec = BulkStringCodec()
    result = await codec.encode("")
    assert result == b"$0\r\n\r\n"

async def test_empty_bulk_string_codec_decode() -> None:
    codec = BulkStringCodec()
    result = await codec.decode(b"$0\r\n\r\n")
    assert result == ""
