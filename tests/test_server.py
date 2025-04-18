import pytest
from strings import EchoService

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


