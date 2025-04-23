import pytest

from crossbill.core import Codec
from crossbill.core.codec import IdentityCodec


class StringCodec(Codec[str, bytes]):
    async def encode(self, data: str) -> bytes:
        return data.encode()

    async def decode(self, data: bytes) -> str:
        return data.decode()


async def test_codec_base_not_implemented() -> None:
    codec = Codec[str, str]()
    with pytest.raises(NotImplementedError):
        _ = await codec.encode("hello")

    with pytest.raises(NotImplementedError):
        _ = await codec.decode("hello")


async def test_codec_encode_decode() -> None:
    codec = StringCodec()
    before = "Simplicity is prerequisite for reliability."
    bytes = await codec.encode(before)
    after = await codec.decode(bytes)
    assert before == after


async def test_codec_decode_encode() -> None:
    codec = StringCodec()
    before = b"\xf0\x9f\xa4\xa9"  # "🤩"
    string = await codec.decode(before)
    after = await codec.encode(string)
    assert before == after


async def test_identity_codec() -> None:
    codec = IdentityCodec()
    value = "Hello World"
    encoded = await codec.encode(value)
    assert value == encoded
    decoded = await codec.decode(value)
    assert value == decoded

    # Ensure the initial value is untouched
    assert value == "Hello World"
