import asyncio

from crossbill.http import (
    HttpClient,
    HttpRequest,
    HttpResponse,
    HttpServer,
    HttpService,
    Status,
)
from crossbill.transport import Address


class HelloHttpService(HttpService):
    async def __call__(self, request: HttpRequest) -> HttpResponse:
        body = "Hello!".encode()
        content_length = len(body)

        response = HttpResponse()
        response.status = Status.OK
        response.headers["Content-Type"] = "text/plain"
        response.headers["Content-Length"] = str(content_length)
        response.body = body

        return response


async def test_strings_e2e() -> None:
    # TODO: Use ephemeral port instead
    address = Address("localhost", 10234)

    server = HttpServer()
    service = HelloHttpService()
    await server.serve(address, service)

    request = HttpRequest()
    request.uri = "/"
    client = HttpClient()
    await client.connect(address)
    response = await client(request)
    text = response.body.decode()
    assert text == "Hello!"

    await client.close()
    await server.close()
