import asyncio

from ..bytes import BytesRequest, BytesResponse
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
    def __init__(
        self, request_codec: RequestCodec, response_codec: ResponseCodec
    ) -> None:
        self.request_codec = request_codec
        self.response_codec = response_codec
        self.reader = None
        self.writer = None

    async def connect(self, address: Address) -> None:
        reader, writer = await asyncio.open_connection(address.host, address.port)
        self.reader = reader
        self.writer = writer

    # TODO: Add abstraction here
    # TODO: Handle errors here
    async def transport(self, request: BytesRequest) -> BytesResponse:
        result = b""
        if self.reader and self.writer:
            self.writer.write(request.value)
            await self.writer.drain()
            result = await self.reader.read(1024)
        return BytesResponse(result)

    async def __call__(self, request: RequestType) -> ResponseType:
        request_bytes = await self.request_codec.encode(request)
        response_bytes = await self.transport(BytesRequest(request_bytes))
        response = await self.response_codec.decode(response_bytes.value)

        return response

    async def close(self) -> None:
        if self.writer:
            self.writer.close()
            await self.writer.wait_closed()
            self.writer = None
            self.reader = None
