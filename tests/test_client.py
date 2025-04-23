from crossbill.string import StringClient, StringRequest


async def test_call_on_empty() -> None:
    client = StringClient()

    # Nothing bad *will* happen here (for now)
    await client(StringRequest("hello"))


async def test_close_on_empty() -> None:
    client = StringClient()

    # Nothing bad should happen here
    await client.close()
