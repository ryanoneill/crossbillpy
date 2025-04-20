import asyncio

from crossbill.core import Filter, FilteredService, Service
from crossbill.string import (
    StringEchoService,
    StringRequest,
    StringResponse,
    StringServer,
)
from crossbill.transport import Address


class DelayFilter(Filter[StringRequest, StringResponse]):
    async def __call__(
        self, request: StringRequest, service: Service[StringRequest, StringResponse]
    ) -> StringResponse:
        await asyncio.sleep(0.01)
        return await service(request)


async def run_echo() -> None:
    address = Address("localhost", 12345)
    server = StringServer()
    service = StringEchoService()
    await server.serve_forever(address, service)
    await server.close()


async def run_delayed() -> None:
    address = Address("localhost", 12345)
    server = StringServer()
    service = StringEchoService()
    filter = DelayFilter()
    filtered = FilteredService(filter, service)
    await server.serve_forever(address, filtered)
    await server.close()


asyncio.run(run_echo())
