"""Module that includes the `Bridge` class."""

from asyncio import StreamReader, StreamWriter

from ..core import Pipeline, ReqRepType


class Bridge(ReqRepType):
    """A `Bridge` is shuffles `bytes` to and from an underlying transport."""

    def __init__(self, pipeline: Pipeline) -> None:
        """Initialize a `Bridge` by supplying a `Pipeline`."""
        self.pipeline = pipeline

    async def __call__(self, reader: StreamReader, writer: StreamWriter) -> None:
        """Asynchronously shuffle `bytes` from a `StreamReader`/`StreamWriter`."""
        while in_data := await reader.read(1024):
            out_data = await self.pipeline(in_data)
            writer.write(out_data)
        writer.close()
        await writer.wait_closed()
