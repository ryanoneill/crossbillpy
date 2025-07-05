from crossbill.redis import BulkErrorCodec


async def test_bulk_error_codec_encode() -> None:
    codec = BulkErrorCodec()
    result = await codec.encode("SYNTAX invalid syntax")
    assert result == b"!21\r\nSYNTAX invalid syntax\r\n"

async def test_bulk_error_codec_decode() -> None:
    codec = BulkErrorCodec()
    result = await codec.decode(b"!21\r\nSYNTAX invalid syntax\r\n")
    assert result == "SYNTAX invalid syntax"
