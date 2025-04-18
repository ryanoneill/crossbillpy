import pytest

from crossbill.string import StringServer


@pytest.mark.asyncio
async def test_close_on_empty() -> None:
    server = StringServer()

    # Nothing bad should happen here
    await server.close()
