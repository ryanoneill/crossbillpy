import asyncio
import pytest
from strings import EchoService

from crossbill.server import Server
from crossbill.string import StringServer
from crossbill.transport import Address


def test_is_running_on_empty() -> None:
    server = StringServer()

    result = server.is_running()
    assert not result


@pytest.mark.asyncio
async def test_is_running_on_running() -> None:
    server = StringServer()
    address = Address("localhost", 10555)
    await server.serve(address, EchoService())
    assert server.is_running()
    await server.close()
    assert not server.is_running()


@pytest.mark.asyncio
async def test_close_on_empty() -> None:
    server = StringServer()

    # Nothing bad should happen here
    await server.close()


@pytest.mark.asyncio
async def test_serve_forever() -> None:
    server = StringServer()
    address = Address("localhost", 10555)
    task = asyncio.create_task(close_serve_forever(server))
    await server.serve_forever(address, EchoService())
    await task


async def close_serve_forever(server: Server) -> None:
    while not server.is_running():
        await asyncio.sleep(0.1)
    assert server.is_running()
    await server.close()
    assert not server.is_running()

