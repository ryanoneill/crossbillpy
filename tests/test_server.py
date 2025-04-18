import asyncio

import pytest
from strings import ReverseService

from crossbill.string import StringServer
from crossbill.transport import Address


async def run_server(address: Address, server: StringServer) -> None:
    service = ReverseService()
    await server.serve(address, service)


# TODO: Move this into Server itself and make it more robust
async def wait_for_server(server: StringServer) -> None:
    while not server.is_running():
        await asyncio.sleep(0.1)


async def send_client_oneshot(address: Address, message: bytes) -> bytes:
    reader, writer = await asyncio.open_connection(address.host, address.port)
    writer.write(message)
    await writer.drain()

    data = await reader.read(1024)

    writer.close()
    await writer.wait_closed()

    return data


@pytest.mark.asyncio
async def test_server() -> None:
    # TODO: Use ephemeral port instead
    address = Address("localhost", 10234)

    server = StringServer()

    _ = asyncio.create_task(run_server(address, server))
    await wait_for_server(server)

    message = b"Hello World!"
    result = await send_client_oneshot(address, message)
    assert result.decode() == "!dlroW olleH"

    await server.close()


@pytest.mark.asyncio
async def test_close_on_empty() -> None:
    server = StringServer()

    # Nothing bad should happen here
    await server.close()
