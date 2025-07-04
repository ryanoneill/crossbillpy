from crossbill.http import HttpStatus


def assert_status(status: HttpStatus, code: int, text: str) -> None:
    assert status.value == code
    assert status.code == code
    assert str(status) == text


def test_informational() -> None:
    assert_status(HttpStatus.CONTINUE, 100, "Continue")
    assert_status(HttpStatus.SWITCHING_PROTOCOLS, 101, "Switching Protocols")
    assert_status(HttpStatus.PROCESSING, 102, "Processing")
    assert_status(HttpStatus.EARLY_HINTS, 103, "Early Hints")


def test_successful() -> None:
    assert_status(HttpStatus.OK, 200, "OK")
    assert_status(HttpStatus.CREATED, 201, "Created")
    assert_status(HttpStatus.ACCEPTED, 202, "Accepted")
    assert_status(
        HttpStatus.NON_AUTHORITATIVE_INFORMATION, 203, "Non-Authoritative Information"
    )
    assert_status(HttpStatus.NO_CONTENT, 204, "No Content")
    assert_status(HttpStatus.RESET_CONTENT, 205, "Reset Content")
    assert_status(HttpStatus.PARTIAL_CONTENT, 206, "Partial Content")
    assert_status(HttpStatus.MULTI_STATUS, 207, "Multi-Status")
    assert_status(HttpStatus.ALREADY_REPORTED, 208, "Already Reported")
    assert_status(HttpStatus.IM_USED, 226, "IM Used")


def test_redirection() -> None:
    assert_status(HttpStatus.MULTIPLE_CHOICES, 300, "Multiple Choices")
    assert_status(HttpStatus.MOVED_PERMANENTLY, 301, "Moved Permanently")
    assert_status(HttpStatus.FOUND, 302, "Found")
    assert_status(HttpStatus.SEE_OTHER, 303, "See Other")
    assert_status(HttpStatus.NOT_MODIFIED, 304, "Not Modified")
    assert_status(HttpStatus.USE_PROXY, 305, "Use Proxy")
    assert_status(HttpStatus.UNUSED, 306, "Unused")
    assert_status(HttpStatus.TEMPORARY_REDIRECT, 307, "Temporary Redirect")
    assert_status(HttpStatus.PERMANENT_REDIRECT, 308, "Permanent Redirect")


def test_client_errors() -> None:
    assert_status(HttpStatus.BAD_REQUEST, 400, "Bad Request")
    assert_status(HttpStatus.UNAUTHORIZED, 401, "Unauthorized")
    assert_status(HttpStatus.PAYMENT_REQUIRED, 402, "Payment Required")
    assert_status(HttpStatus.FORBIDDEN, 403, "Forbidden")
    assert_status(HttpStatus.NOT_FOUND, 404, "Not Found")
    assert_status(HttpStatus.METHOD_NOT_ALLOWED, 405, "Method Not Allowed")
    assert_status(HttpStatus.NOT_ACCEPTABLE, 406, "Not Acceptable")
    assert_status(
        HttpStatus.PROXY_AUTHENTICATION_REQUIRED, 407, "Proxy Authentication Required"
    )
    assert_status(HttpStatus.REQUEST_TIMEOUT, 408, "Request Timeout")
    assert_status(HttpStatus.CONFLICT, 409, "Conflict")
    assert_status(HttpStatus.GONE, 410, "Gone")
    assert_status(HttpStatus.LENGTH_REQUIRED, 411, "Length Required")
    assert_status(HttpStatus.PRECONDITION_FAILED, 412, "Precondition Failed")
    assert_status(HttpStatus.CONTENT_TOO_LARGE, 413, "Content Too Large")
    assert_status(HttpStatus.URI_TOO_LONG, 414, "URI Too Long")
    assert_status(HttpStatus.UNSUPPORTED_MEDIA_TYPE, 415, "Unsupported Media Type")
    assert_status(HttpStatus.RANGE_NOT_SATISFIABLE, 416, "Range Not Satisfiable")
    assert_status(HttpStatus.EXPECTATION_FAILED, 417, "Expectation Failed")
    assert_status(HttpStatus.IM_A_TEAPOT, 418, "I'm a Teapot")
    assert_status(HttpStatus.MISDIRECTED_REQUEST, 421, "Misdirected Request")
    assert_status(HttpStatus.UNPROCESSABLE_CONTENT, 422, "Unprocessable Content")
    assert_status(HttpStatus.LOCKED, 423, "Locked")
    assert_status(HttpStatus.FAILED_DEPENDENCY, 424, "Failed Dependency")
    assert_status(HttpStatus.TOO_EARLY, 425, "Too Early")
    assert_status(HttpStatus.UPGRADE_REQUIRED, 426, "Upgrade Required")
    assert_status(HttpStatus.PRECONDITION_REQUIRED, 428, "Precondition Required")
    assert_status(HttpStatus.TOO_MANY_REQUESTS, 429, "Too Many Requests")
    assert_status(
        HttpStatus.REQUEST_HEADER_FIELDS_TOO_LARGE,
        431,
        "Request Header Fields Too Large",
    )
    assert_status(
        HttpStatus.UNAVAILABLE_FOR_LEGAL_REASONS, 451, "Unavailable for Legal Reasons"
    )


def test_server_errors() -> None:
    assert_status(HttpStatus.INTERNAL_SERVER_ERROR, 500, "Internal Server Error")
    assert_status(HttpStatus.NOT_IMPLEMENTED, 501, "Not Implemented")
    assert_status(HttpStatus.BAD_GATEWAY, 502, "Bad Gateway")
    assert_status(HttpStatus.SERVICE_UNAVAILABLE, 503, "Service Unavailable")
    assert_status(HttpStatus.GATEWAY_TIMEOUT, 504, "Gateway Timeout")
    assert_status(
        HttpStatus.HTTP_VERSION_NOT_SUPPORTED, 505, "HTTP Version Not Supported"
    )
    assert_status(HttpStatus.VARIANT_ALSO_NEGOTIATES, 506, "Variant Also Negotiates")
    assert_status(HttpStatus.INSUFFICIENT_STORAGE, 507, "Insufficient Storage")
    assert_status(HttpStatus.LOOP_DETECTED, 508, "Loop Detected")
    assert_status(HttpStatus.NOT_EXTENDED, 510, "Not Extended")
    assert_status(
        HttpStatus.NETWORK_AUTHENTICATION_REQUIRED,
        511,
        "Network Authentication Required",
    )
