import pytest

from crossbill.core import PipelineFactory

from strings import ReverseService, StringPipelineFactory


@pytest.mark.asyncio
async def test_abstract_pipeline_factory() -> None:
    pipeline_factory = PipelineFactory()
    service = ReverseService()
    with pytest.raises(NotImplementedError):
        await pipeline_factory(service)


@pytest.mark.asyncio
async def test_pipeline_factory() -> None:
    pipeline_factory = StringPipelineFactory()
    service = ReverseService()

    pipeline = await pipeline_factory(service)

    bytes = "Hello World!".encode()
    result = await pipeline(bytes)
    assert result.decode() == "!dlroW olleH"
