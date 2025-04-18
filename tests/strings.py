from crossbill.core import (
    Pipeline,
    PipelineFactory,
    Service,
)

from crossbill.string import (
    StringRequest,
    StringResponse,
    StringRequestCodec,
    StringResponseCodec,
)


class EchoService(Service[StringRequest, StringResponse]):
    async def __call__(self, request: StringRequest) -> StringResponse:
        return StringResponse(request.value)


class ReverseService(Service[StringRequest, StringResponse]):
    async def __call__(self, request: StringRequest) -> StringResponse:
        return StringResponse(request.value[::-1])


class SpamService(Service[StringRequest, StringResponse]):
    async def __call__(self, request: StringRequest) -> StringResponse:
        return StringResponse("spam")


class StringPipelineFactory(PipelineFactory):
    async def __call__(self, service: Service) -> Pipeline:
        request_codec = StringRequestCodec()
        response_codec = StringResponseCodec()
        pipeline = Pipeline(request_codec, response_codec, service)
        return pipeline


class StringPipeline(Pipeline[StringRequest, StringResponse]):
    def __init__(self) -> None:
        super().__init__(StringRequestCodec(), StringResponseCodec(), EchoService())
