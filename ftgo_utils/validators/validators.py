import string
import validators
from .exceptions import (
    PasswordValidationError, InvalidEmailFormatError, PhoneNumberFormatError
)

def validate_email(email: str):
    if not email:
        return email
    try:
        email = email.strip()
        if validators.email(email):
            return email
        raise ValueError("")
    except Exception as e:
        raise ValueError(str(InvalidEmailFormatError(email)))

def validate_phone_number(phone_number: str):
    try:
        phone_number = phone_number.strip().replace(" ", "")
        if phone_number.startswith("+98"):
            phone_number = phone_number[3:]
        elif phone_number.startswith("98"):
            phone_number = phone_number[2:]
            
        if phone_number.startswith("09"):
            phone_number = phone_number[1:]
        elif phone_number.startswith("9"):
            pass
        else:
            raise ValueError("Invalid phone number format")
        
        if not phone_number.isdigit():
            raise ValueError("Phone number should only contain numbers")
        
        if len(phone_number) != 10:
            raise ValueError("Phone number should be 10 digits long")
        
        return phone_number
    except ValueError as e:
        raise ValueError(str(PhoneNumberFormatError(phone_number, message=str(e.args[0]))))

def validate_password(password: str):
    try:
        if not password:
            raise ValueError("Password cannot be empty")
        
        if len(password) < 8:
            raise ValueError("Password should be at least 8 characters long")
        
        if not any(char.isdigit() for char in password):
            raise ValueError("Password should contain at least one digit")
        
        if not any(char.isupper() for char in password):
            raise ValueError("Password should contain at least one uppercase letter")
        
        if not any(char.islower() for char in password):
            raise ValueError("Password should contain at least one lowercase letter")
        
        if not any(char in string.punctuation for char in password):
            raise ValueError("Password should contain at least one special character")

        return password
    except ValueError as e:
        raise ValueError(str(PasswordValidationError(password, message=str(e.args[0]))))
