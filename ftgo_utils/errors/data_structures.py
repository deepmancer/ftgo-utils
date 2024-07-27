import json
from enum import Enum
from typing import Optional, Union

from pydantic import BaseModel, Field, field_validator


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
    RESOURCE_LIMIT_ERROR = 'resource_limit_error'
    GENERIC_ERROR = 'generic_error'


class ErrorCode(BaseModel):
    value: str = Field(...)
    category: Optional[Union[ErrorCategory, str]] = Field(default=ErrorCategory.GENERIC_ERROR.value)
    status_code: Optional[int] = Field(None)
    description: Optional[str] = Field(None, alias='message')

    class Config:
        frozen = True

    @field_validator('category', pre=True)
    def validate_category_field(cls, value):
        if not value:
            return ErrorCategory.GENERIC_ERROR
        if isinstance(value, Enum):
            value = value.value

        if not isinstance(value, str):
            raise ValueError("Invalid category type")

        if value not in {category.value for category in ErrorCategory}:
            raise ValueError("Invalid category value")

        return value

    def __str__(self) -> str:
        return self.to_json()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.to_json()})"

    def to_dict(self) -> dict:
        return self.dict(exclude_none=True)

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str, indent=4)

__all__ = ["ErrorCode", "ErrorCategory"]
