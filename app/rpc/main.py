from typing import Any

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from jsonrpc import JSONRPCResponseManager, dispatcher

import app.rpc.methods  # noqa: F401  # pyright: ignore[reportUnusedImport]

app = FastAPI()


@app.post("/api", response_model=None)
async def handle_rpc(request: Request) -> dict[str, Any] | JSONResponse:
    body: bytes = await request.body()
    request_str: str = body.decode("utf-8")
    response = JSONRPCResponseManager.handle(request_str, dispatcher)
    if response is None:
        return JSONResponse(status_code=204, content=None)
    data = response.data
    if isinstance(data, list):
        return JSONResponse(content=data)
    return data
