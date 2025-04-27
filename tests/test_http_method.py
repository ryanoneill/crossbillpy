from crossbill.http import Method


def assert_method(method: Method, text: str) -> None:
    assert str(method) == text
    assert method.value == text
    assert method.verb == text


def test_get() -> None:
    assert_method(Method.GET, "GET")


def test_head() -> None:
    assert_method(Method.HEAD, "HEAD")


def test_post() -> None:
    assert_method(Method.POST, "POST")


def test_put() -> None:
    assert_method(Method.PUT, "PUT")


def test_delete() -> None:
    assert_method(Method.DELETE, "DELETE")


def test_connect() -> None:
    assert_method(Method.CONNECT, "CONNECT")


def test_options() -> None:
    assert_method(Method.OPTIONS, "OPTIONS")


def test_trace() -> None:
    assert_method(Method.TRACE, "TRACE")


def test_patch() -> None:
    assert_method(Method.PATCH, "PATCH")
