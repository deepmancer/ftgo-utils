import json
from enum import Enum
from typing import Optional, Union

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

class ErrorCode:
    def __init__(
        self,
        value: str,
        category: Optional[Union[ErrorCategory, str]] = ErrorCategory.GENERIC_ERROR,
        status_code: Optional[int] = None,
        description: Optional[str] = None,
    ):
        self._value = value
        self._category = category.value if isinstance(category, ErrorCategory) else str(category)
        self._status_code = status_code
        self._description = description
        
    @property
    def value(self) -> str:
        return self._value
    
    @property
    def category(self) -> str:
        return self._category
    
    @property
    def status_code(self) -> Optional[int]:
        return self._status_code
    
    @property
    def description(self) -> Optional[str]:
        return self._description

    def to_dict(self) -> dict:
        error_code_details = {
            "value": self.value,
            "category": self.category,
            "status_code": self.status_code,
            "description": self.description,
        }
        return {k: v for k, v in error_code_details.items() if v is not None}

    def toJSON(self) -> str:
        return json.dumps(self.to_dict(), indent=4, default=vars)
    
    def to_json(self) -> str:
        return self.toJSON()
