import json
from typing import List

from crossbill.http import HttpRequest, HttpRequestCodec, HttpMethod


async def test_encode() -> None:
    codec = HttpRequestCodec()

    request = HttpRequest()
    request.method = HttpMethod.POST
    request.uri = "/"
    request.headers["Host"] = "developer.mozilla.org"
    request.headers["User-Agent"] = "curl/8.6.0"
    request.headers["Accept"] = "*/*"
    request.headers["Content-Type"] = "application/json"
    request.headers["Content-Length"] = "345"
    request.body = '{ "data": "ABC123" }'.encode()

    bytes = await codec.encode(request)
    lines = bytes.split(b"\r\n")
    assert lines[0] == "POST / HTTP/1.1".encode()
    headers = set(lines[1:6])
    print(headers)
    assert "Host: developer.mozilla.org".encode() in headers
    assert "User-Agent: curl/8.6.0".encode() in headers
    assert "Accept: */*".encode() in headers
    assert "Content-Type: application/json".encode() in headers
    assert "Content-Length: 345".encode() in headers

    body = json.loads(lines[7].decode())
    assert body["data"] == "ABC123"


async def test_decode() -> None:
    codec = HttpRequestCodec()

    lines: List[str] = []
    lines.append("POST / HTTP/1.1")
    lines.append("Host: developer.mozilla.org")
    lines.append("User-Agent: curl/8.6.0")
    lines.append("Accept: */*")
    lines.append("Content-Type: application/json")
    lines.append("Content-Length: 345")
    lines.append("")
    lines.append('{ "data": "ABC123" }')

    bytes = ("\r\n".join(lines)).encode()

    request = await codec.decode(bytes)

    assert request.method == HttpMethod.POST
    assert request.uri == "/"
    assert len(request.headers) == 5
    assert request.headers["Host"] == "developer.mozilla.org"
    assert request.headers["User-Agent"] == "curl/8.6.0"
    assert request.headers["Accept"] == "*/*"
    assert request.headers["Content-Type"] == "application/json"
    assert request.headers["Content-Length"] == "345"

    body = json.loads(request.body.decode())
    assert body["data"] == "ABC123"


async def test_decode_no_body() -> None:
    codec = HttpRequestCodec()

    lines: List[str] = []
    lines.append("GET / HTTP/1.1")
    lines.append("Host: example.com")
    lines.append("User-Agent: curl/8.6.0")
    lines.append("Accept: text/html,application/json")
    lines.append("")
    lines.append("")

    bytes = ("\r\n".join(lines)).encode()
    print(bytes)

    request = await codec.decode(bytes)

    assert request.method == HttpMethod.GET
    assert request.uri == "/"
    assert len(request.headers) == 3
    assert request.headers["Host"] == "example.com"
    assert request.headers["User-Agent"] == "curl/8.6.0"
    assert request.headers["Accept"] == "text/html,application/json"

    assert request.body == b""
