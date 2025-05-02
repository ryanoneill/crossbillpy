from crossbill.http import HttpMethod


def assert_method(method: HttpMethod, text: str) -> None:
    assert str(method) == text
    assert method.value == text
    assert method.verb == text


def test_get() -> None:
    assert_method(HttpMethod.GET, "GET")


def test_head() -> None:
    assert_method(HttpMethod.HEAD, "HEAD")


def test_post() -> None:
    assert_method(HttpMethod.POST, "POST")


def test_put() -> None:
    assert_method(HttpMethod.PUT, "PUT")


def test_delete() -> None:
    assert_method(HttpMethod.DELETE, "DELETE")


def test_connect() -> None:
    assert_method(HttpMethod.CONNECT, "CONNECT")


def test_options() -> None:
    assert_method(HttpMethod.OPTIONS, "OPTIONS")


def test_trace() -> None:
    assert_method(HttpMethod.TRACE, "TRACE")


def test_patch() -> None:
    assert_method(HttpMethod.PATCH, "PATCH")
