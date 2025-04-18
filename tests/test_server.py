import asyncio

import pytest
from strings import ReverseService

from crossbill.string import StringClient, StringRequest, StringServer
from crossbill.transport import Address


@pytest.mark.asyncio
async def test_server() -> None:
    # TODO: Use ephemeral port instead
    address = Address("localhost", 10234)

    server = StringServer()
    await server.serve(address, ReverseService())

    message = "Hello World!"
    client = StringClient()
    await client.connect(address)
    response = await client(StringRequest(message))
    assert response.value == "!dlroW olleH"

    await client.close()
    await server.close()


@pytest.mark.asyncio
async def test_close_on_empty() -> None:
    server = StringServer()

    # Nothing bad should happen here
    await server.close()
