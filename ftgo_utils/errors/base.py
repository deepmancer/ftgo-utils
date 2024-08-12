import json
import time
import uuid
from typing import Any, Dict, Optional, Union

from .data_structures import ErrorCode


class BaseError(Exception):
    def __init__(
        self,
        error_code: ErrorCode,
        payload: Optional[Dict[str, Any]] = None,
        message: Optional[str] = None,
        timestamp: Optional[Union[float, int]] = None,
        issuer: Optional[str] = None,
        **kwargs
    ):
        super().__init__(message or error_code.to_json())
        self.error_id = uuid.uuid4().hex
        self.error_code = error_code
        self.payload = payload or {}
        self.message = message
        self.timestamp = int(timestamp) if timestamp is not None else int(time.time())
        self.issuer = issuer

    def __str__(self) -> str:
        return self.to_json()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.to_json()})"

    def to_dict(self) -> Dict[str, Any]:
        error_details = {
            "error_id": self.error_id,
            "error_code": self.error_code.to_dict(),
            "message": self.message,
            "payload": self.payload,
            "timestamp": self.timestamp,
            "issuer": self.issuer,
        }
        return {k: v for k, v in error_details.items() if v is not None}

    def toJSON(self) -> str:
        return json.dumps(self.to_dict(), indent=4, default=str)
    
    def to_json(self) -> str:
        return self.toJSON()

__all__ = ["BaseError"]
