from typing import Optional


class ValidationError(Exception):
    def __init__(self, message: str, details: Optional[str] = None):
        final_message = f"{message}\nDetails: {details}" if details else message
        super().__init__(final_message)


class PhoneNumberFormatError(ValidationError):
    def __init__(self, phone_number: str, message: Optional[str] = None):
        base_message = f"Phone number {phone_number} is not in the correct format"
        super().__init__(base_message, message)

class PasswordValidationError(ValidationError):
    def __init__(self, password: str, message: Optional[str] = None):
        base_message = f"Error: Password {password} is not valid"
        super().__init__(base_message, message)

class InvalidEmailFormatError(ValidationError):
    def __init__(self, email: str, message: Optional[str] = None):
        base_message = f"Error: Email {email} is not in the correct format"
        super().__init__(base_message, message)
