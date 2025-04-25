"""Module that includes the `Bridge` class."""

from asyncio import Event, StreamReader, StreamWriter
import asyncio

from ..core import Closable, Pipeline, ReqRepType


class Bridge(Closable, ReqRepType):
    """A `Bridge` is shuffles `bytes` to and from an underlying transport."""

    def __init__(self, pipeline: Pipeline) -> None:
        """Initialize a `Bridge` by supplying a `Pipeline`."""
        self.pipeline = pipeline
        self._exiting = Event()


    async def __call__(self, reader: StreamReader, writer: StreamWriter) -> None:
        """Asynchronously shuffle `bytes` from a `StreamReader`/`StreamWriter`."""
        while not self._exiting.is_set():
            try:
                async with asyncio.timeout(0.1):
                    in_data = await reader.read(1024)
                if in_data != b"":
                    out_data = await self.pipeline(in_data)
                    writer.write(out_data)
                else:
                    break
            except TimeoutError:
                pass
        writer.close()
        await writer.wait_closed()


    async def close(self) -> None:
        self._exiting.set()
