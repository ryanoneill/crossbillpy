from crossbill.core import Pipeline, Service
from crossbill.string import (
    StringEchoService,
    StringRequest,
    StringRequestCodec,
    StringResponse,
    StringResponseCodec,
)


class ReverseService(Service[StringRequest, StringResponse]):
    async def __call__(self, request: StringRequest) -> StringResponse:
        return StringResponse(request.value[::-1])


class SpamService(Service[StringRequest, StringResponse]):
    async def __call__(self, request: StringRequest) -> StringResponse:
        return StringResponse("spam")


class StringPipeline(Pipeline[StringRequest, StringResponse]):
    def __init__(self) -> None:
        super().__init__(
            StringRequestCodec(), StringResponseCodec(), StringEchoService()
        )
