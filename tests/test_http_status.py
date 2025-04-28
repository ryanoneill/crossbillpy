from crossbill.http import Status


def assert_status(status: Status, code: int, text: str) -> None:
    assert status.value == code
    assert status.code == code
    assert str(status) == text


def test_informational() -> None:
    assert_status(Status.CONTINUE, 100, "Continue")
    assert_status(Status.SWITCHING_PROTOCOLS, 101, "Switching Protocols")
    assert_status(Status.PROCESSING, 102, "Processing")
    assert_status(Status.EARLY_HINTS, 103, "Early Hints")


def test_successful() -> None:
    assert_status(Status.OK, 200, "OK")
    assert_status(Status.CREATED, 201, "Created")
    assert_status(Status.ACCEPTED, 202, "Accepted")
    assert_status(
        Status.NON_AUTHORITATIVE_INFORMATION, 203, "Non-Authoritative Information"
    )
    assert_status(Status.NO_CONTENT, 204, "No Content")
    assert_status(Status.RESET_CONTENT, 205, "Reset Content")
    assert_status(Status.PARTIAL_CONTENT, 206, "Partial Content")
    assert_status(Status.MULTI_STATUS, 207, "Multi-Status")
    assert_status(Status.ALREADY_REPORTED, 208, "Already Reported")
    assert_status(Status.IM_USED, 226, "IM Used")


def test_redirection() -> None:
    assert_status(Status.MULTIPLE_CHOICES, 300, "Multiple Choices")
    assert_status(Status.MOVED_PERMANENTLY, 301, "Moved Permanently")
    assert_status(Status.FOUND, 302, "Found")
    assert_status(Status.SEE_OTHER, 303, "See Other")
    assert_status(Status.NOT_MODIFIED, 304, "Not Modified")
    assert_status(Status.USE_PROXY, 305, "Use Proxy")
    assert_status(Status.UNUSED, 306, "Unused")
    assert_status(Status.TEMPORARY_REDIRECT, 307, "Temporary Redirect")
    assert_status(Status.PERMANENT_REDIRECT, 308, "Permanent Redirect")


def test_client_errors() -> None:
    assert_status(Status.BAD_REQUEST, 400, "Bad Request")
    assert_status(Status.UNAUTHORIZED, 401, "Unauthorized")
    assert_status(Status.PAYMENT_REQUIRED, 402, "Payment Required")
    assert_status(Status.FORBIDDEN, 403, "Forbidden")
    assert_status(Status.NOT_FOUND, 404, "Not Found")
    assert_status(Status.METHOD_NOT_ALLOWED, 405, "Method Not Allowed")
    assert_status(Status.NOT_ACCEPTABLE, 406, "Not Acceptable")
    assert_status(
        Status.PROXY_AUTHENTICATION_REQUIRED, 407, "Proxy Authentication Required"
    )
    assert_status(Status.REQUEST_TIMEOUT, 408, "Request Timeout")
    assert_status(Status.CONFLICT, 409, "Conflict")
    assert_status(Status.GONE, 410, "Gone")
    assert_status(Status.LENGTH_REQUIRED, 411, "Length Required")
    assert_status(Status.PRECONDITION_FAILED, 412, "Precondition Failed")
    assert_status(Status.CONTENT_TOO_LARGE, 413, "Content Too Large")
    assert_status(Status.URI_TOO_LONG, 414, "URI Too Long")
    assert_status(Status.UNSUPPORTED_MEDIA_TYPE, 415, "Unsupported Media Type")
    assert_status(Status.RANGE_NOT_SATISFIABLE, 416, "Range Not Satisfiable")
    assert_status(Status.EXPECTATION_FAILED, 417, "Expectation Failed")
    assert_status(Status.IM_A_TEAPOT, 418, "I'm a Teapot")
    assert_status(Status.MISDIRECTED_REQUEST, 421, "Misdirected Request")
    assert_status(Status.UNPROCESSABLE_CONTENT, 422, "Unprocessable Content")
    assert_status(Status.LOCKED, 423, "Locked")
    assert_status(Status.FAILED_DEPENDENCY, 424, "Failed Dependency")
    assert_status(Status.TOO_EARLY, 425, "Too Early")
    assert_status(Status.UPGRADE_REQUIRED, 426, "Upgrade Required")
    assert_status(Status.PRECONDITION_REQUIRED, 428, "Precondition Required")
    assert_status(Status.TOO_MANY_REQUESTS, 429, "Too Many Requests")
    assert_status(
        Status.REQUEST_HEADER_FIELDS_TOO_LARGE, 431, "Request Header Fields Too Large"
    )
    assert_status(
        Status.UNAVAILABLE_FOR_LEGAL_REASONS, 451, "Unavailable for Legal Reasons"
    )


def test_server_errors() -> None:
    assert_status(Status.INTERNAL_SERVER_ERROR, 500, "Internal Server Error")
    assert_status(Status.NOT_IMPLEMENTED, 501, "Not Implemented")
    assert_status(Status.BAD_GATEWAY, 502, "Bad Gateway")
    assert_status(Status.SERVICE_UNAVAILABLE, 503, "Service Unavailable")
    assert_status(Status.GATEWAY_TIMEOUT, 504, "Gateway Timeout")
    assert_status(Status.HTTP_VERSION_NOT_SUPPORTED, 505, "HTTP Version Not Supported")
    assert_status(Status.VARIANT_ALSO_NEGOTIATES, 506, "Variant Also Negotiates")
    assert_status(Status.INSUFFICIENT_STORAGE, 507, "Insufficient Storage")
    assert_status(Status.LOOP_DETECTED, 508, "Loop Detected")
    assert_status(Status.NOT_EXTENDED, 510, "Not Extended")
    assert_status(
        Status.NETWORK_AUTHENTICATION_REQUIRED, 511, "Network Authentication Required"
    )
