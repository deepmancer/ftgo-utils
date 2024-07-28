import json
from dataclasses import dataclass
from typing import Optional, Union

@dataclass(frozen=True)
class ErrorCategory:
    value: str
    status_code: Optional[int] = 500

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return self.value

    def __eq__(self, other) -> bool:
        if isinstance(other, ErrorCategory):
            return self.value == other.value
        if isinstance(other, str):
            return self.value == other
        return False

class ErrorCode:
    def __init__(
        self,
        value: str,
        category: Optional[Union[ErrorCategory, str]] = ErrorCategory("UNKNOWN_ERROR"),
        status_code: Optional[int] = None,
        description: Optional[str] = None,
    ):
        self._value = value
        self._category = category.value if isinstance(category, ErrorCategory) else str(category)
        self._status_code = status_code if status_code is not None else category.status_code
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

    def __str__(self) -> str:
        return self.to_json()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.to_json()})"

    def to_json(self) -> str:
        return json.dumps(self.to_dict())
