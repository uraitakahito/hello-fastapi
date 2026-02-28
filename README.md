## Starting the development servers

### Hello World server (port 8000)

```console
% uv run uvicorn app.hello.main:app --reload --host 0.0.0.0 --port 8000
```

### JSON-RPC server (port 8001)

```console
% uv run uvicorn app.rpc.main:app --reload --host 0.0.0.0 --port 8001
```

## Testing with curl

### Hello World server

```console
% curl http://localhost:8000/
{"Hello":"World"}
```

### JSON-RPC server

```console
% curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc": "2.0", "method": "subtract", "params": {"minuend": 42, "subtrahend": 23}, "id": 1}' \
  http://localhost:8001/api
{"jsonrpc": "2.0", "result": 19.0, "id": 1}
```

## Running the tests

```console
% uv run pytest
```

## Starting the development server with Docker

If you develop inside a Docker container, run the following commands and read the documentation at the top of the Dockerfile to set up your development environment.

```console
% curl -L -O https://raw.githubusercontent.com/uraitakahito/hello_python_uv/refs/tags/1.0.0/Dockerfile
% curl -L -O https://raw.githubusercontent.com/uraitakahito/hello_python_uv/refs/tags/1.0.0/docker-entrypoint.sh
% chmod 755 docker-entrypoint.sh
```
