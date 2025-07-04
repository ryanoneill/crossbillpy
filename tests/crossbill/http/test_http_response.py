from crossbill.http import HttpResponse, HttpStatus


def test_response() -> None:
    # This API is not expected to remain as is.
    # It is unfinished.
    response = HttpResponse()

    assert response.headers["Location"] == ""
    assert response.body == b""
    assert response.status == HttpStatus.OK

    response.headers["Location"] = "http://www.example.com/users/123"
    response.body = b"body content"
    response.status = HttpStatus.FOUND

    assert response.headers["Location"] == "http://www.example.com/users/123"
    assert response.body == b"body content"
    assert response.status == HttpStatus.FOUND
