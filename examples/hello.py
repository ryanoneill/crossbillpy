import asyncio

from crossbill.string import (
    StringClient,
    StringEchoService,
    StringRequest,
    StringServer,
)
from crossbill.transport import Address


async def main() -> None:
    address = Address("localhost", 12345)
    server = StringServer()
    await server.serve(address, StringEchoService())

    message = "Hello from crossbill-demo!"
    client = StringClient()
    await client.connect(address)
    response = await client(StringRequest(message))
    print(response.value)

    await client.close()
    await server.close()


if __name__ == "__main__":
    asyncio.run(main())
