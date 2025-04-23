import asyncio

from strings import ReverseService

from crossbill.string import StringClient, StringRequest, StringServer
from crossbill.transport import Address


async def test_strings_e2e() -> None:
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


async def test_strings_connect_only() -> None:
    # TODO: Use ephemeral port instead
    address = Address("localhost", 10234)

    server = StringServer()
    await server.serve(address, ReverseService())

    client = StringClient()

    await client.connect(address)
    await asyncio.sleep(0.1)
    await client.close()

    await server.close()
