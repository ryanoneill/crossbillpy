"""Module that provides the `HttpStatus` class."""

from enum import IntEnum


class HttpStatus(IntEnum):
    """Representation of an HTTP Response Status and associated code."""

    # Informational Responses
    CONTINUE = 100
    SWITCHING_PROTOCOLS = 101
    PROCESSING = 102
    EARLY_HINTS = 103

    # Successful Responses
    OK = 200
    CREATED = 201
    ACCEPTED = 202
    NON_AUTHORITATIVE_INFORMATION = 203
    NO_CONTENT = 204
    RESET_CONTENT = 205
    PARTIAL_CONTENT = 206
    MULTI_STATUS = 207
    ALREADY_REPORTED = 208
    IM_USED = 226

    # Redirection Messages
    MULTIPLE_CHOICES = 300
    MOVED_PERMANENTLY = 301
    FOUND = 302
    SEE_OTHER = 303
    NOT_MODIFIED = 304
    USE_PROXY = 305
    UNUSED = 306
    TEMPORARY_REDIRECT = 307
    PERMANENT_REDIRECT = 308

    # Client Error Responses
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    PAYMENT_REQUIRED = 402
    FORBIDDEN = 403
    NOT_FOUND = 404
    METHOD_NOT_ALLOWED = 405
    NOT_ACCEPTABLE = 406
    PROXY_AUTHENTICATION_REQUIRED = 407
    REQUEST_TIMEOUT = 408
    CONFLICT = 409
    GONE = 410
    LENGTH_REQUIRED = 411
    PRECONDITION_FAILED = 412
    CONTENT_TOO_LARGE = 413
    URI_TOO_LONG = 414
    UNSUPPORTED_MEDIA_TYPE = 415
    RANGE_NOT_SATISFIABLE = 416
    EXPECTATION_FAILED = 417
    IM_A_TEAPOT = 418
    MISDIRECTED_REQUEST = 421
    UNPROCESSABLE_CONTENT = 422
    LOCKED = 423
    FAILED_DEPENDENCY = 424
    TOO_EARLY = 425
    UPGRADE_REQUIRED = 426
    PRECONDITION_REQUIRED = 428
    TOO_MANY_REQUESTS = 429
    REQUEST_HEADER_FIELDS_TOO_LARGE = 431
    UNAVAILABLE_FOR_LEGAL_REASONS = 451

    # Server Error Responses
    INTERNAL_SERVER_ERROR = 500
    NOT_IMPLEMENTED = 501
    BAD_GATEWAY = 502
    SERVICE_UNAVAILABLE = 503
    GATEWAY_TIMEOUT = 504
    HTTP_VERSION_NOT_SUPPORTED = 505
    VARIANT_ALSO_NEGOTIATES = 506
    INSUFFICIENT_STORAGE = 507
    LOOP_DETECTED = 508
    NOT_EXTENDED = 510
    NETWORK_AUTHENTICATION_REQUIRED = 511

    @property
    def code(self) -> int:
        """Return the code associated with the `HttpStatus`."""
        return self.value

    def __str__(self) -> str:
        """Return the text associated with the `HttpStatus`."""
        result: str = ""
        match self.code:
            case 100:
                result = "Continue"
            case 101:
                result = "Switching Protocols"
            case 102:
                result = "Processing"
            case 103:
                result = "Early Hints"
            case 200:
                result = "OK"
            case 201:
                result = "Created"
            case 202:
                result = "Accepted"
            case 203:
                result = "Non-Authoritative Information"
            case 204:
                result = "No Content"
            case 205:
                result = "Reset Content"
            case 206:
                result = "Partial Content"
            case 207:
                result = "Multi-Status"
            case 208:
                result = "Already Reported"
            case 226:
                result = "IM Used"
            case 300:
                result = "Multiple Choices"
            case 301:
                result = "Moved Permanently"
            case 302:
                result = "Found"
            case 303:
                result = "See Other"
            case 304:
                result = "Not Modified"
            case 305:
                result = "Use Proxy"
            case 306:
                result = "Unused"
            case 307:
                result = "Temporary Redirect"
            case 308:
                result = "Permanent Redirect"
            case 400:
                result = "Bad Request"
            case 401:
                result = "Unauthorized"
            case 402:
                result = "Payment Required"
            case 403:
                result = "Forbidden"
            case 404:
                result = "Not Found"
            case 405:
                result = "Method Not Allowed"
            case 406:
                result = "Not Acceptable"
            case 407:
                result = "Proxy Authentication Required"
            case 408:
                result = "Request Timeout"
            case 409:
                result = "Conflict"
            case 410:
                result = "Gone"
            case 411:
                result = "Length Required"
            case 412:
                result = "Precondition Failed"
            case 413:
                result = "Content Too Large"
            case 414:
                result = "URI Too Long"
            case 415:
                result = "Unsupported Media Type"
            case 416:
                result = "Range Not Satisfiable"
            case 417:
                result = "Expectation Failed"
            case 418:
                result = "I'm a Teapot"
            case 421:
                result = "Misdirected Request"
            case 422:
                result = "Unprocessable Content"
            case 423:
                result = "Locked"
            case 424:
                result = "Failed Dependency"
            case 425:
                result = "Too Early"
            case 426:
                result = "Upgrade Required"
            case 428:
                result = "Precondition Required"
            case 429:
                result = "Too Many Requests"
            case 431:
                result = "Request Header Fields Too Large"
            case 451:
                result = "Unavailable for Legal Reasons"
            case 500:
                result = "Internal Server Error"
            case 501:
                result = "Not Implemented"
            case 502:
                result = "Bad Gateway"
            case 503:
                result = "Service Unavailable"
            case 504:
                result = "Gateway Timeout"
            case 505:
                result = "HTTP Version Not Supported"
            case 506:
                result = "Variant Also Negotiates"
            case 507:
                result = "Insufficient Storage"
            case 508:
                result = "Loop Detected"
            case 510:
                result = "Not Extended"
            case 511:
                result = "Network Authentication Required"
            case _:  # pragma: no cover
                result = ""

        return result
