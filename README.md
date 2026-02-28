## Starting the development server

```console
% uv run fastapi dev
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
