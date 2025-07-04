import pytest

from crossbill.bytes import BytesPipelineFactory
from crossbill.core import PipelineFactory
from crossbill.string import StringPipelineFactory, StringRequest, StringResponse
from tests.bytes import BytesEchoService
from tests.strings import ReverseService


async def test_abstract_pipeline_factory() -> None:
    pipeline_factory: PipelineFactory[StringRequest, StringResponse] = PipelineFactory()
    service = ReverseService()
    with pytest.raises(NotImplementedError):
        await pipeline_factory(service)


async def test_string_pipeline_factory() -> None:
    pipeline_factory = StringPipelineFactory()
    service = ReverseService()

    pipeline = await pipeline_factory(service)

    bytes = "Hello World!".encode()
    result = await pipeline(bytes)
    assert result.decode() == "!dlroW olleH"


async def test_bytes_pipeline_factory() -> None:
    pipeline_factory = BytesPipelineFactory()
    service = BytesEchoService()

    pipeline = await pipeline_factory(service)

    bytes = "Hello World!".encode()
    result = await pipeline(bytes)
    assert result.decode() == "Hello World!"
