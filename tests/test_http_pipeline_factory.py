from crossbill.http import (
    HttpPipelineFactory,
    HttpRequest,
    HttpResponse,
    HttpService,
    HttpStatus,
)


class HttpNoContentService(HttpService):
    async def __call__(self, request: HttpRequest) -> HttpResponse:
        response = HttpResponse()
        response.status = HttpStatus.NO_CONTENT
        return response


async def test_http_pipeline_factory() -> None:
    pipeline_factory = HttpPipelineFactory()
    service = HttpNoContentService()
    pipeline = await pipeline_factory(service)
    request = "GET / HTTP/1.1\r\n\r\n".encode()
    response = await pipeline(request)
    assert response.decode() == "HTTP/1.1 204 No Content\r\n\r\n"
