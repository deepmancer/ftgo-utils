from .base import Dict

from ._driver import DriverErrorCodes
from ._infrastructure import InfraErrorCodes
from ._user import UserErrorCodes
from ._validation import ValidationErrorCodes

ErrorCodes = Dict(
    **InfraErrorCodes,
    **UserErrorCodes,
    **DriverErrorCodes,
    **ValidationErrorCodes,
)
