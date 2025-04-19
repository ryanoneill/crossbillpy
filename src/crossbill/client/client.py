"""Module that contains the `Client` class."""

import asyncio

from ..core import (
    Closable,
    ReqRepType,
    RequestCodec,
    RequestType,
    ResponseCodec,
    ResponseType,
)
from ..transport import Address


class Client(Closable, ReqRepType):
    """A `Client` sends `Request`s and receives `Response`s from `Server`s."""

    def __init__(
        self, request_codec: RequestCodec, response_codec: ResponseCodec
    ) -> None:
        """Initialize a `Client` based on the included `Codec`s."""
        self.request_codec = request_codec
        self.response_codec = response_codec
        self.reader = None
        self.writer = None

    async def connect(self, address: Address) -> None:
        """Connect to the `Address` so that `Request`s may be sent."""
        reader, writer = await asyncio.open_connection(address.host, address.port)
        self.reader = reader
        self.writer = writer

    # TODO: Add abstraction here
    # TODO: Handle errors here
    async def _transport(self, data: bytes) -> bytes:
        result = b""
        if self.reader and self.writer:
            self.writer.write(data)
            await self.writer.drain()
            result = await self.reader.read(1024)
        return result

    async def __call__(self, request: RequestType) -> ResponseType:
        """Asynchronously sends a `Request` and receives a `Response`."""
        request_bytes = await self.request_codec.encode(request)
        response_bytes = await self._transport(request_bytes)
        response = await self.response_codec.decode(response_bytes)

        return response

    async def close(self) -> None:
        """Close a `Client`. If not connected, that's ok."""
        if self.writer:
            self.writer.close()
            await self.writer.wait_closed()
            self.writer = None
            self.reader = None
