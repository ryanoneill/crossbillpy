"""Module that includes the `Server` class."""

import asyncio
from asyncio import Server as AsyncioServer
from asyncio import Task
from asyncio.exceptions import CancelledError
from typing import Generic, Optional

from ..core import Closable, PipelineFactory, RequestType, ResponseType, Service
from ..transport import Address, Bridge


class Server(Closable, Generic[RequestType, ResponseType]):
    """A `Server` handles `Request`s and returns `Response`s to `Client`s."""

    def __init__(
        self, pipeline_factory: PipelineFactory[RequestType, ResponseType]
    ) -> None:
        """Initialize a `Server`.

        The `PipelineFactory` is used to create a `Pipeline` from the
        `Service` that is provided via the `serve` method.
        """
        self.pipeline_factory = pipeline_factory
        self.server: Optional[AsyncioServer] = None
        self._run_task: Optional[Task[None]] = None
        self._bridge: Optional[Bridge[RequestType, ResponseType]] = None

    def is_running(self) -> bool:
        """Returns `True` if the `Server` is running, `False` otherwise."""
        result = False
        if self.server:
            result = self.server.is_serving()
        return result

    async def _run(self, server: AsyncioServer) -> None:
        try:
            async with server:
                await server.serve_forever()
        except CancelledError:
            pass

    async def _setup(
        self, address: Address, service: Service[RequestType, ResponseType]
    ) -> AsyncioServer:
        pipeline = await self.pipeline_factory(service)
        self._bridge = Bridge(pipeline)
        return await asyncio.start_server(self._bridge, address.host, address.port)

    async def serve(
        self, address: Address, service: Service[RequestType, ResponseType]
    ) -> None:
        """Start listening on the given `Address` and pass requests to `Service`."""
        self.server = await self._setup(address, service)
        # Don't assign the created task to '_'. That's a mistake
        # Doing so allows the background run task to be collected, which
        # is undesirable.
        self._run_task = asyncio.create_task(self._run(self.server))
        await self.server.start_serving()

    async def serve_forever(
        self, address: Address, service: Service[RequestType, ResponseType]
    ) -> None:
        """Start listening on the given `Address` and pass requests to `Service`.

        This method differs from `serve` in that the `Coroutine` returned will
        not be done until the `Server` shuts down.
        """
        self.server = await self._setup(address, service)
        await self._run(self.server)

    async def close(self) -> None:
        """Close a `Server`. If not running, that's ok."""
        if self.server:
            if self._bridge:
                await self._bridge.close()
                self._bridge = None
            self.server.close()
            await self.server.wait_closed()
            self.server = None
