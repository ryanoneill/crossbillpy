import json
from typing import List

from crossbill.http import HttpResponse, HttpResponseCodec, HttpStatus


async def test_encode() -> None:
    codec = HttpResponseCodec()

    response = HttpResponse()
    response.status = HttpStatus.FORBIDDEN
    response.headers["Server"] = "Apache"
    response.headers["Date"] = "Fri, 21 Jun 2024 12:52:39 GMT"
    response.headers["Content-Length"] = "345"
    response.headers["Content-Type"] = "application/json"
    response.headers["Cache-Control"] = "no-store"

    response.body = '{ "data": "ABC123" }'.encode()

    bytes = await codec.encode(response)
    lines = bytes.split(b"\r\n")
    assert lines[0] == "HTTP/1.1 403 Forbidden".encode()
    headers = set(lines[1:6])
    print(headers)
    assert "Server: Apache".encode() in headers
    assert "Date: Fri, 21 Jun 2024 12:52:39 GMT".encode() in headers
    assert "Content-Length: 345".encode() in headers
    assert "Content-Type: application/json".encode() in headers
    assert "Cache-Control: no-store".encode() in headers

    body = json.loads(lines[7].decode())
    assert body["data"] == "ABC123"


async def test_decode() -> None:
    codec = HttpResponseCodec()

    lines: List[str] = []
    lines.append("HTTP/1.1 403 Forbidden")
    lines.append("Server: Apache")
    lines.append("Date: Fri, 21 Jun 2024 12:52:39 GMT")
    lines.append("Content-Type: application/json")
    lines.append("Content-Length: 345")
    lines.append("Cache-Control: no-store")
    lines.append("")
    lines.append('{ "data": "ABC123" }')

    bytes = ("\r\n".join(lines)).encode()

    response = await codec.decode(bytes)

    assert response.status == HttpStatus.FORBIDDEN
    assert len(response.headers) == 5
    assert response.headers["Server"] == "Apache"
    assert response.headers["Date"] == "Fri, 21 Jun 2024 12:52:39 GMT"
    assert response.headers["Content-Type"] == "application/json"
    assert response.headers["Content-Length"] == "345"
    assert response.headers["Cache-Control"] == "no-store"

    body = json.loads(response.body.decode())
    assert body["data"] == "ABC123"


async def test_decode_no_body() -> None:
    codec = HttpResponseCodec()

    lines: List[str] = []
    lines.append("HTTP/1.1 403 Forbidden")
    lines.append("Server: Apache")
    lines.append("Date: Fri, 21 Jun 2024 12:52:39 GMT")
    lines.append("Content-Type: application/json")
    lines.append("Cache-Control: no-store")
    lines.append("")
    lines.append("")

    bytes = ("\r\n".join(lines)).encode()

    response = await codec.decode(bytes)

    assert response.status == HttpStatus.FORBIDDEN
    assert len(response.headers) == 4
    assert response.headers["Server"] == "Apache"
    assert response.headers["Date"] == "Fri, 21 Jun 2024 12:52:39 GMT"
    assert response.headers["Content-Type"] == "application/json"
    assert response.headers["Cache-Control"] == "no-store"

    assert response.body == b""


async def test_chunked_response() -> None:
    codec = HttpResponseCodec()

    lines: List[str] = []
    lines.append("HTTP/1.1 200 OK")
    lines.append("Date: Fri, 02 May 2025 17:05:44 GMT")
    lines.append("Expires: -1")
    lines.append("Cache-Control: private, max-age=0")
    lines.append("Content-Type: text/html; charset=ISO-8859-1")
    lines.append("Transfer-Encoding: chunked")
    lines.append("")
    lines.append("<html><body><h1>Hello</h1></body></html>")

    bytes = ("\r\n".join(lines)).encode()

    response = await codec.decode(bytes)

    assert response.status == HttpStatus.OK
    assert len(response.headers) == 5
    assert response.headers["Date"] == "Fri, 02 May 2025 17:05:44 GMT"
    assert response.headers["Expires"] == "-1"
    assert response.headers["Cache-Control"] == "private, max-age=0"
    assert response.headers["Content-Type"] == "text/html; charset=ISO-8859-1"
    assert response.headers["Transfer-Encoding"] == "chunked"

    assert response.body.decode() == "<html><body><h1>Hello</h1></body></html>"
