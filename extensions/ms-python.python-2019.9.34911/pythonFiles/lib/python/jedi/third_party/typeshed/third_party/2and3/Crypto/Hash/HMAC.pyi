from typing import Any, Optional

digest_size: Any

class HMAC:
    digest_size: Any
    digestmod: Any
    outer: Any
    inner: Any
    def __init__(self, key, msg: Optional[Any] = ..., digestmod: Optional[Any] = ...) -> None: ...
    def update(self, msg): ...
    def copy(self): ...
    def digest(self): ...
    def hexdigest(self): ...

def new(key, msg: Optional[Any] = ..., digestmod: Optional[Any] = ...): ...
