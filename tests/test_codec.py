import pytest

from crossbill.core import Codec

class StringCodec(Codec[str, bytes]):
    async def encode(self, data: str) -> bytes:
        return data.encode()

    async def decode(self, data: bytes) -> str:
        return data.decode()


@pytest.mark.anyio
async def test_codec_encode_decode() -> None:
    codec = StringCodec()
    before = "Simplicity is prerequisite for reliability."
    bytes = await codec.encode(before)
    after = await codec.decode(bytes)
    assert before == after

@pytest.mark.anyio
async def test_codec_decode_encode() -> None:
    codec = StringCodec()
    before = b"\xf0\x9f\xa4\xa9" # "🤩"
    string = await codec.decode(before)
    after = await codec.encode(string)
    assert before == after
