from typing import Optional

class PostgresConnectionError(Exception):
    def __init__(self, url: str, message: Optional[str] = None,):
        base_message = f"Error: Failed to connect to postgres at {url}"
        message = f"Details: {message}"
        final_message = f"{base_message}\n{message}"
        super().__init__(final_message)

class PostgresSessionCreationError(Exception):
    def __init__(self, url: str, message: Optional[str] = None):
        base_message = f"Error: Failed to create a postgres session at {url}"
        message = f"Details: {message}"
        final_message = f"{base_message}\n{message}"
        super().__init__(final_message)
