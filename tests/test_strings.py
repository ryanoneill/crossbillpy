import pytest
from strings import ReverseService

from crossbill.string import StringClient, StringRequest, StringServer
from crossbill.transport import Address


@pytest.mark.asyncio
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


