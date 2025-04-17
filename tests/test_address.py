from crossbill.transport import Address


def test_address() -> None:
    address = Address("localhost", 1234)
    assert address.host == "localhost"
    assert address.port == 1234
