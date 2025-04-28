from crossbill.http import HttpRequest, Method


def test_request() -> None:
    # This API is not expected to remain as is.
    # It is unfinished.
    request = HttpRequest()

    assert request.headers["Host"] == ""
    assert request.body == b""
    assert request.method == Method.GET
    assert request.uri == "/"

    request.headers["Host"] = "localhost"
    request.body = "body content".encode()
    request.method = Method.POST
    request.uri = "/abcd"

    assert request.headers["Host"] == "localhost"
    assert request.body == b"body content"
    assert request.method == Method.POST
    assert request.uri == "/abcd"
