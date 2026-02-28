from collections.abc import Callable
from typing import Any, TypeVar, overload

_F = TypeVar("_F", bound=Callable[..., Any])

class Dispatcher:
    def __init__(
        self, prototype: dict[str, Callable[..., Any]] | object | None = None
    ) -> None: ...
    @overload
    def add_method(
        self,
        f: _F,
        name: str | None = None,
        context_arg: str | None = None,
    ) -> _F: ...
    @overload
    def add_method(
        self,
        f: None = None,
        name: str | None = None,
        context_arg: str | None = None,
    ) -> Callable[[_F], _F]: ...
    def __getitem__(self, key: str) -> Callable[..., Any]: ...
    def __setitem__(self, key: str, value: Callable[..., Any]) -> None: ...
    def __delitem__(self, key: str) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Any: ...
    def __contains__(self, key: object) -> bool: ...

class JSONRPC20Response:
    @property
    def data(self) -> dict[str, Any]: ...

class JSONRPC20BatchResponse:
    @property
    def data(self) -> list[dict[str, Any]]: ...

class JSONRPCResponseManager:
    @classmethod
    def handle(
        cls,
        request_str: str | bytes,
        dispatcher: Dispatcher,
        context: dict[str, Any] | None = None,
    ) -> JSONRPC20Response | JSONRPC20BatchResponse | None: ...

dispatcher: Dispatcher
