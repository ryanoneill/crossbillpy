import asyncio
import pytest
from asyncio import Server

from crossbill.transport import Bridge

from strings import StringPipeline


async def run_server(server):
    async with server:
        await server.serve_forever()

async def create_server(host: str, port: int, bridge: Bridge) -> Server:
    server = await asyncio.start_server(bridge, host, port)
    return server

async def close_server(server: Server) -> None:
    server.close()
    await server.wait_closed()

async def send_client_oneshot(host: str, port: int, message: bytes) -> bytes:
    reader, writer = await asyncio.open_connection(host, port)
    writer.write(message)
    await writer.drain()

    data = await reader.read(1024)

    writer.close()
    await writer.wait_closed()

    return data

@pytest.mark.asyncio
async def test_bridge():
    host = "localhost"
    port = 10234 # TODO: Use ephemeral port instead

    pipeline = StringPipeline()
    bridge = Bridge(pipeline)

    server = await create_server(host, port, bridge)
    _ = asyncio.create_task(run_server(server))

    message = b"Hello World!"
    result = await send_client_oneshot(host, port, message)
    assert result == message

    await close_server(server)
