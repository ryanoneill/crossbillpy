from crossbill.core import (
    Pipeline,
    PipelineFactory,
    Request,
    RequestCodec,
    Response,
    ResponseCodec,
    Service,
)


class StringRequest(Request):
    def __init__(self, value: str) -> None:
        self.value = value


class StringResponse(Response):
    def __init__(self, value: str) -> None:
        self.value = value


class StringRequestCodec(RequestCodec[StringRequest]):
    async def encode(self, data: StringRequest) -> bytes:
        return data.value.encode()

    async def decode(self, data: bytes) -> StringRequest:
        return StringRequest(data.decode())


class StringResponseCodec(ResponseCodec[StringResponse]):
    async def encode(self, data: StringResponse) -> bytes:
        return data.value.encode()

    async def decode(self, data: bytes) -> StringResponse:
        return StringResponse(data.decode())


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
