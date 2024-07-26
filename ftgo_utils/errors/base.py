import json
from typing import Optional, Dict, Any
import uuid


class BaseError(Exception):
    def __init__(
        self, 
        error_code: str = "GENERIC_ERROR", 
        message: Optional[str] = None, 
        payload: Optional[Dict[str, Any]] = None,
        *args, 
        **kwargs,
    ):
        super().__init__(message, *args, **kwargs)
        self.error_id = str(uuid.uuid4())
        self.error_code = error_code
        self.message = message or "An error occurred."
        self.payload = payload or {}

    def __str__(self):
        error_details = {
            "error_id": self.error_id,
            "error_code": self.error_code,
            "message": self.message,
            "payload": self.payload,
        }
        return json.dumps(error_details, default=str, indent=4)

    def to_dict(self) -> Dict[str, Any]:
        """Convert the error details to a dictionary."""
        return {
            "error_id": self.error_id,
            "error_code": self.error_code,
            "message": self.message,
            "payload": self.payload,
        }

    def to_json(self) -> str:
        """Convert the error details to a JSON string."""
        return json.dumps(self.to_dict(), default=str, indent=4)
