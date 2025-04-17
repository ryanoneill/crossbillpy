"""Module that includes the `Server` class."""

import asyncio
from asyncio import Server as AsyncioServer
from typing import Optional

from ..core import Closable, ReqRepType, Service, PipelineFactory
from ..transport import Address, Bridge


class Server(Closable, ReqRepType):
    """A `Server` handles `Request`s and returns `Response`s to `Client`s."""

    def __init__(self, pipeline_factory: PipelineFactory) -> None:
        """Initialize a `Server`.

        The `PipelineFactory` is used to create a `Pipeline` from the
        `Service` that is provided via the `serve` method.
        """
        self.pipeline_factory = pipeline_factory
        self.server: Optional[AsyncioServer] = None

    def is_running(self) -> bool:
        """Returns `True` if the `Server` is running, `False` otherwise."""
        result = False
        if self.server:
            result = self.server.is_serving()
        return result

    async def serve(self, address: Address, service: Service) -> None:
        """Start listening on the given `Address` and pass requests to `Service`."""
        pipline = await self.pipeline_factory(service)
        bridge = Bridge(pipline)
        self.server = await asyncio.start_server(bridge, address.host, address.port)
        async with self.server:
            await self.server.serve_forever()

    async def close(self) -> None:
        """Close a `Server`. If not running, that's ok."""
        if self.server:
            self.server.close()
            await self.server.wait_closed()
            self.server = None
