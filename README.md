# Crossbill

## Description

Crossbill is a Python library focused on building Finagle-style `Service`-based
asynchronous clients and servers. It is very much a work in progress, and as
such, does not follow semantic versioning, nor should the APIs be considered
stable.

## Getting Started

Crossbill is published to PyPI. Here's a walkthrough of how to include it as a
dependency in your project via `uv`.

### Create a New Project

```shell
$ uv init crossbill-demo
$ cd crossbill-demo
```

### Add Crossbill as a Dependency

```shell
$ uv add crossbill
```

### Code the Example

By default, `uv` will generate a `hello.py` file. Replace its contents with the
following code:

```python
import asyncio
from crossbill.core import Service
from crossbill.string import (
    StringClient,
    StringRequest,
    StringResponse,
    StringServer,
)
from crossbill.transport import Address


class EchoService(Service[StringRequest, StringResponse]):
    async def __call__(self, request: StringRequest) -> StringResponse:
        return StringResponse(request.value)


async def main() -> None:
    address = Address("localhost", 12345)
    server = StringServer()
    await server.serve(address, EchoService())

    message = "Hello from crossbill-demo!"
    client = StringClient()
    await client.connect(address)
    response = await client(StringRequest(message))
    print(response.value)

    await client.close()
    await server.close()


if __name__ == "__main__":
    asyncio.run(main())
```

### Run the Example

```shell
$ uv run hello.py
Hello from crossbill-demo!
```

## Development

The `crossbill` project uses `uv`, "[a]n extremely fast Python package and
project manager, written in Rust." If you don't have it installed, follow
the [installation guide](https://docs.astral.sh/uv/getting-started/installation/)
in order to do so.

### Dependency Installation

With `uv` installed, run the following from the command line to ensure that all
dependencies are properly installed.

```shell
$ uv sync
```
### Testing

This project uses `pytest` along with `asyncio` in order to run asynchronous
tests. A predominant number of tests within this library will fit that criteria
due to the nature of the domain space. 

To run the existing unit tests, run the following from the command line.

```shell
$ uv run pytest
```

#### Coverage

This project uses `coverage` and `pytest-cov` for measuring code coverage. To
generate the report when running tests, run the following from the command line.

```shell
$ uv run pytest --cov
```
