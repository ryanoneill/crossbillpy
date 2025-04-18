import asyncio

import pytest
from strings import ReverseService

from crossbill.string import StringClient, StringRequest, StringServer
from crossbill.transport import Address


async def run_server(address: Address, server: StringServer) -> None:
    service = ReverseService()
    await server.serve(address, service)


# TODO: Move this into Server itself and make it more robust
async def wait_for_server(server: StringServer) -> None:
    while not server.is_running():
        await asyncio.sleep(0.1)


@pytest.mark.asyncio
async def test_server() -> None:
    # TODO: Use ephemeral port instead
    address = Address("localhost", 10234)

    server = StringServer()

    _ = asyncio.create_task(run_server(address, server))
    await wait_for_server(server)

    message = "Hello World!"
    client = StringClient()
    await client.connect(address)
    response = await client(StringRequest(message))
    assert response.value == "!dlroW olleH"

    await client.close()
    await server.close()


@pytest.mark.asyncio
async def test_call_on_empty() -> None:
    client = StringClient()

    # Nothing bad *will* happen here (for now)
    await client(StringRequest("hello"))


@pytest.mark.asyncio
async def test_close_on_empty() -> None:
    client = StringClient()

    # Nothing bad should happen here
    await client.close()
