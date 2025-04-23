from bytes import BytesEchoService

from crossbill.bytes import BytesClient, BytesRequest, BytesServer
from crossbill.transport import Address


async def test_bytes_e2e() -> None:
    # TODO: Use ephemeral port instead
    address = Address("localhost", 10234)

    server = BytesServer()
    await server.serve(address, BytesEchoService())

    message = b"Hello World!"
    client = BytesClient()
    await client.connect(address)
    response = await client(BytesRequest(message))
    assert response.value == b"Hello World!"

    await client.close()
    await server.close()
