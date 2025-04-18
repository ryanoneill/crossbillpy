from ..client import Client
from .request import StringRequest
from .request_codec import StringRequestCodec
from .response import StringResponse
from .response_codec import StringResponseCodec


class StringClient(Client[StringRequest, StringResponse]):
    def __init__(self) -> None:
        request_codec = StringRequestCodec()
        response_codec = StringResponseCodec()
        super().__init__(request_codec, response_codec)
