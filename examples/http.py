import asyncio

from crossbill.http import (
    HttpClient,
    HttpEchoService,
    HttpRequest,
    HttpResponse,
    HttpServer,
)
from crossbill.transport import Address


async def main() -> None:
    address = Address("localhost", 12345)
    server = HttpServer()
    await server.serve(address, HttpEchoService())

    message = "Hello from crossbill-demo!"
    encoded = message.encode()
    request = HttpRequest()
    request.uri = "/"
    request.headers["Content-Type"] = "text/plain"
    request.headers["Content-Length"] = str(len(encoded))
    request.body = encoded

    client = HttpClient()
    await client.connect(address)
    response: HttpResponse = await client(request)
    result = response.body.decode()
    assert result == message
    print(result)

    await client.close()
    await server.close()


if __name__ == "__main__":
    asyncio.run(main())
