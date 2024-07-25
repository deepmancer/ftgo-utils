from typing import Optional

class BaseError(Exception):
    scope: Optional[str] = None

    def __init__(self, error_code: str, *args, **kwargs):
        self.error_code = error_code
        super().__init__(*args, **kwargs)
