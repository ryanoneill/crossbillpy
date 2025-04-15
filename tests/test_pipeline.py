import pytest

from crossbill.core import Pipeline

from strings import EchoService, SpamService, StringRequestCodec, StringResponseCodec


@pytest.mark.anyio
async def test_pipeline() -> None:
    request_codec = StringRequestCodec()
    response_codec = StringResponseCodec()
    service = EchoService()
    pipeline = Pipeline(request_codec, response_codec, service)

    bytes = "Hello World!".encode()
    result = await pipeline(bytes)
    assert result == bytes
    assert result.decode() == "Hello World!"


@pytest.mark.anyio
async def test_pipeline_spam() -> None:
    request_codec = StringRequestCodec()
    response_codec = StringResponseCodec()
    service = SpamService()
    pipeline = Pipeline(request_codec, response_codec, service)

    # The `SpamService` returns "spam" regardless of the input
    # This is to ensure that the request is properly reaching
    # the backend `Service`.
    bytes = "Hello World!".encode()
    result = await pipeline(bytes)
    expected = "spam"
    assert result == expected.encode()
    assert result.decode() == expected
