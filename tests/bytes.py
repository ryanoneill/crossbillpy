from crossbill.bytes import BytesRequest, BytesResponse
from crossbill.core import Service


class BytesEchoService(Service[BytesRequest, BytesResponse]):
    async def __call__(self, request: BytesRequest) -> BytesResponse:
        return BytesResponse(request.value)
