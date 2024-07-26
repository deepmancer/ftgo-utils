import json
from typing import Optional, Dict, Any
import uuid


class BaseError(Exception):
    def __init__(
        self, 
        error_code: str = "GENERIC_ERROR", 
        payload: Optional[Dict[str, Any]] = None,
        message: Optional[str] = None, 
        *args, 
        **kwargs,
    ):
        super().__init__(message, *args, **kwargs)
        self.error_id = str(uuid.uuid4())
        self.error_code = error_code
        self.payload = payload or {}
        self.message = message

    def __str__(self):
        return json.dumps(self.to_dict(), default=str, indent=4)

    def to_dict(self) -> Dict[str, Any]:
        error_details = {
            "error_id": self.error_id,
            "error_code": self.error_code,
            "message": self.message,
            "payload": self.payload,
        }
        return {k: v for k, v in error_details.items() if v is not None}

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str, indent=4)
