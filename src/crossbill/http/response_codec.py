"""Module that includes the `HttpResponseCodec` class."""

from io import BytesIO

from ..core import ResponseCodec
from .response import HttpResponse
from .status import HttpStatus


class HttpResponseCodec(ResponseCodec[HttpResponse]):
    """An `HttpResponseCodec` converts between `bytes` and an `HttpResponse`."""

    async def encode(self, data: HttpResponse) -> bytes:
        """Convert from an `HttpResponse` to `bytes`."""
        writer = bytearray()

        await self._write_response_line(writer, data)
        await self._write_response_headers(writer, data)
        await self._write_response_body(writer, data)

        return bytes(writer)

    async def decode(self, data: bytes) -> HttpResponse:
        """Convert from `bytes` to an `HttpResponse`."""
        reader = BytesIO(data)
        result = HttpResponse()

        await self._read_response_line(reader, result)
        await self._read_response_headers(reader, result)
        await self._read_response_body(reader, result)

        return result

    async def _read_response_line(
        self, reader: BytesIO, response: HttpResponse
    ) -> None:
        # TODO: Make more robust
        raw_response_line = reader.readline()
        response_line = raw_response_line.decode()
        parts = response_line.split(" ")
        status = HttpStatus(int(parts[1]))
        response.status = status

    async def _read_response_headers(
        self, reader: BytesIO, response: HttpResponse
    ) -> None:
        # TODO: Make more robust
        # * Handle Improper HTTP Headers
        # * Handle Multiple Headers with the Same Name
        # * Handle Ensuring That We Don't Infinitely Loop
        # * Handle a Max Response Size
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
                response.headers[header] = value

    async def _read_response_body(
        self, reader: BytesIO, response: HttpResponse
    ) -> None:
        # TODO: Make more robust
        # * Handle `Content-Length` not being title cased.
        # * Handle Reader not able to read requested number of bytes.
        # * Handle `Transfer-Encoding` chunked better.
        if "Content-Length" in response.headers:
            length = int(response.headers["Content-Length"])
            response.body = reader.read(length)
        else:
            body = b""
            while (in_data := reader.read(1)) != b"":
                body += in_data
            response.body = body

    async def _write_response_line(
        self, writer: bytearray, response: HttpResponse
    ) -> None:
        writer.extend("HTTP/1.1 ".encode())
        writer.extend(str(response.status.code).encode())
        writer.extend(b" ")
        writer.extend(str(response.status).encode())
        writer.extend(b"\r\n")

    async def _write_response_headers(
        self, writer: bytearray, response: HttpResponse
    ) -> None:
        for header, value in response.headers.items():
            writer.extend(header.encode())
            writer.extend(b": ")
            writer.extend(value.encode())
            writer.extend(b"\r\n")
        writer.extend(b"\r\n")

    async def _write_response_body(
        self, writer: bytearray, response: HttpResponse
    ) -> None:
        writer.extend(response.body)
