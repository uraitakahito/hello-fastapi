from fastapi import FastAPI, Request
from jsonrpc import JSONRPCResponseManager, dispatcher  # type: ignore[import-untyped]

import app.rpc.methods  # noqa: F401  # Register JSON-RPC methods

app = FastAPI()


@app.post("/api")
async def handle_rpc(request: Request) -> dict:
    body: bytes = await request.body()
    request_str: str = body.decode("utf-8")
    response = JSONRPCResponseManager.handle(request_str, dispatcher)
    return response.data
