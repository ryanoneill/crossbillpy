import math

from crossbill.redis import DoubleCodec


async def test_pos_double_codec_encode() -> None:
    codec = DoubleCodec()
    result = await codec.encode(1.23)
    assert result == b",1.23\r\n"

async def test_pos_double_codec_decode() -> None:
    codec = DoubleCodec()
    result = await codec.decode(b",1.23\r\n")
    assert math.isclose(result, 1.23)

async def test_neg_double_codec_encode() -> None:
    codec = DoubleCodec()
    result = await codec.encode(-1.23)
    assert result == b",-1.23\r\n"

async def test_neg_double_codec_decode() -> None:
    codec = DoubleCodec()
    result = await codec.decode(b",-1.23\r\n")
    assert math.isclose(result, -1.23)

async def test_zero_double_codec_encode() -> None:
    codec = DoubleCodec()
    result = await codec.encode(0)
    assert result == b",0\r\n"

async def test_zero_double_codec_decode() -> None:
    codec = DoubleCodec()
    result = await codec.decode(b",0\r\n")
    assert math.isclose(result, 0)
    
async def test_inf_double_codec_encode() -> None:
    codec = DoubleCodec()
    result = await codec.encode(float("inf"))
    assert result == b",inf\r\n"

async def test_inf_double_codec_decode() -> None:
    codec = DoubleCodec()
    result = await codec.decode(b",inf\r\n")
    assert result == float("inf")

async def test_neg_inf_double_codec_encode() -> None:
    codec = DoubleCodec()
    result = await codec.encode(float("-inf"))
    assert result == b",-inf\r\n"

async def test_neg_inf_double_codec_decode() -> None:
    codec = DoubleCodec()
    result = await codec.decode(b",-inf\r\n")
    assert result == float("-inf")

async def test_nan_double_codec_encode() -> None:
    codec = DoubleCodec()
    result = await codec.encode(float("nan"))
    assert result == b",nan\r\n"

async def test_nan_double_codec_decode() -> None:
    codec = DoubleCodec()
    result = await codec.decode(b",nan\r\n")
    assert math.isnan(result)

async def test_pos_exp_double_codec_decode() -> None:
    codec = DoubleCodec()
    result = await codec.decode(b",-1.23E+8\r\n")
    assert math.isclose(result, -123000000.0)

async def test_neg_exp_double_codec_decode() -> None:
    codec = DoubleCodec()
    result = await codec.decode(b",-1.23E-8\r\n")
    assert math.isclose(result, -0.0000000123)
