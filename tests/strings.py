from crossbill.core import Request, RequestCodec, Response, ResponseCodec, Service


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
