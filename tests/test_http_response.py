from crossbill.http import HttpResponse, Status


def test_response() -> None:
    # This API is not expected to remain as is.
    # It is unfinished.
    response = HttpResponse()

    assert response.headers["Location"] == ""
    assert response.body == b""
    assert response.status == Status.OK

    response.headers["Location"] = "http://www.example.com/users/123"
    response.body = b"body content"
    response.status = Status.FOUND

    assert response.headers["Location"] == "http://www.example.com/users/123"
    assert response.body == b"body content"
    assert response.status == Status.FOUND
