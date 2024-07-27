import json
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field

class ErrorCategory(str, Enum):
    CLIENT_ERROR = 'client_error'
    SERVER_ERROR = 'server_error'
    DOMAIN_ERROR = 'domain_error'
    MESSAGE_BROKER_ERROR = 'message_broker_error'
    VALIDATION_ERROR = 'validation_error'
    DATABASE_ERROR = 'database_error'
    CACHE_ERROR = 'cache_error'
    RABBITMQ_ERROR = 'rabbitmq_error'
    NETWORK_ERROR = 'network_error'
    CONNECTION_ERROR = 'connection_error'
    RESOURCE_LIMIT_ERROR = 'resource_limit_error'
    GENERIC_ERROR = 'generic_error'

class ErrorCode(BaseModel):
    value: str = Field(...)
    category: Optional[ErrorCategory] = Field(default=ErrorCategory.GENERIC_ERROR)
    status_code: Optional[int] = Field(None)
    description: Optional[str] = Field(None)

    class Config:
        frozen = True

    def to_dict(self) -> dict:
        return self.dict(exclude_none=True)

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=4)

__all__ = ["ErrorCode", "ErrorCategory"]
