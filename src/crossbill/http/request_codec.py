"""Module that includes the `HttpRequestCodec` class."""

from io import BytesIO

from ..core import RequestCodec
from .method import HttpMethod
from .request import HttpRequest


class HttpRequestCodec(RequestCodec[HttpRequest]):
    """An `HttpRequestCodec` converts between `bytes` and an `HttpRequest`."""

    async def encode(self, data: HttpRequest) -> bytes:
        """Convert from an `HttpRequest` to `bytes`."""
        writer = bytearray()

        await self._write_request_line(writer, data)
        await self._write_request_headers(writer, data)
        await self._write_request_body(writer, data)

        return bytes(writer)

    async def decode(self, data: bytes) -> HttpRequest:
        """Convert from `bytes` to an `HttpRequest`."""
        reader = BytesIO(data)
        result = HttpRequest()

        await self._read_request_line(reader, result)
        await self._read_request_headers(reader, result)
        await self._read_request_body(reader, result)

        return result

    async def _read_request_line(self, reader: BytesIO, request: HttpRequest) -> None:
        # TODO: Make more robust
        raw_request_line = reader.readline()
        request_line = raw_request_line.decode()
        parts = request_line.split(" ")
        request.method = HttpMethod(parts[0].upper())
        request.uri = parts[1]

    async def _read_request_headers(
        self, reader: BytesIO, request: HttpRequest
    ) -> None:
        # TODO: Make more robust
        # * Handle Improper HTTP Headers
        # * Handle Multiple Headers with the Same Name
        # * Handle Ensuring That We Don't Infinitely Loop
        # * Handle a Max Request Size
        done = False
        while not done:
            buffer = b""
            while buffer[-2:] != b"\r\n":
                buffer += reader.read(1)
            if buffer == b"\r\n":
                done = True
            else:
                line = buffer.decode().rstrip()
                pos = line.find(":")
                header = line[:pos]
                value = line[pos + 1 :].lstrip()
                request.headers[header] = value

    async def _read_request_body(self, reader: BytesIO, request: HttpRequest) -> None:
        # TODO: Make more robust
        # * Handle `Content-Length` not being title cased.
        # * Handle Reader not able to read requested number of bytes.
        if "Content-Length" in request.headers:
            length = int(request.headers["Content-Length"])
            request.body = reader.read(length)

    async def _write_request_line(
        self, writer: bytearray, request: HttpRequest
    ) -> None:
        writer.extend(request.method.encode())
        writer.extend(b" ")
        writer.extend(request.uri.encode())
        writer.extend(b" HTTP/1.1\r\n")

    async def _write_request_headers(
        self, writer: bytearray, request: HttpRequest
    ) -> None:
        for header, value in request.headers.items():
            writer.extend(header.encode())
            writer.extend(b": ")
            writer.extend(value.encode())
            writer.extend(b"\r\n")
        writer.extend(b"\r\n")

    async def _write_request_body(
        self, writer: bytearray, request: HttpRequest
    ) -> None:
        writer.extend(request.body)
