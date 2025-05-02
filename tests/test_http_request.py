from crossbill.http import HttpMethod, HttpRequest


def test_request() -> None:
    # This API is not expected to remain as is.
    # It is unfinished.
    request = HttpRequest()

    assert request.headers["Host"] == ""
    assert request.body == b""
    assert request.method == HttpMethod.GET
    assert request.uri == "/"

    request.headers["Host"] = "localhost"
    request.body = "body content".encode()
    request.method = HttpMethod.POST
    request.uri = "/abcd"

    assert request.headers["Host"] == "localhost"
    assert request.body == b"body content"
    assert request.method == HttpMethod.POST
    assert request.uri == "/abcd"


def test_request_uri_constructor() -> None:
    request = HttpRequest("/hello")
    assert request.uri == "/hello"
