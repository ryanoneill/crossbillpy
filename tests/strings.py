from crossbill.core import Request, Response, Service


class StringRequest(Request):
    def __init__(self, value: str) -> None:
        self.value = value


class StringResponse(Response):
    def __init__(self, value: str) -> None:
        self.value = value


class EchoService(Service[StringRequest, StringResponse]):
    async def __call__(self, request: StringRequest) -> StringResponse:
        return StringResponse(request.value)
