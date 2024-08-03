import json
from typing import Optional, Union

from .data_structures import ErrorCategory, ErrorCode

class ErrorCategories:
    UNKNOWN_ERROR = ErrorCategory(
        value='UNKNOWN_ERROR',
        status_code=500,
    )
    BUSINESS_LOGIC_ERROR = ErrorCategory(
        value='BUSINESS_LOGIC_ERROR',
        status_code=400,
    )
    IO_ERROR = ErrorCategory(
        value='IO_ERROR',
        status_code=500,
    )

    @classmethod
    def get_error_category(cls, error_category: str) -> ErrorCategory:
        return getattr(cls, error_category.upper(), cls.UNKNOWN_ERROR)

class ErrorCodes:
    UNKNOWN_ERROR = ErrorCode(
        value="UNKNOWN_ERROR",
        category=ErrorCategories.UNKNOWN_ERROR,
        description="An unknown error has occurred.",
    )
    # Field Validation Errors
    MISSING_PHONE_NUMBER_ERROR = ErrorCode(
        value="MISSING_PHONE_NUMBER_ERROR",
        category=ErrorCategories.BUSINESS_LOGIC_ERROR,
        status_code=400,
        description="Phone number is missing.",
    )
    INVALID_PHONE_NUMBER_ERROR = ErrorCode(
        value="INVALID_PHONE_NUMBER_ERROR",
        category=ErrorCategories.BUSINESS_LOGIC_ERROR,
        status_code=400,
        description="Phone number is invalid.",
    )
    MISSING_NATIONAL_ID_ERROR = ErrorCode(
        value="MISSING_NATIONAL_ID_ERROR",
        category=ErrorCategories.BUSINESS_LOGIC_ERROR,
        status_code=400,
        description="National ID is missing.",
    )
    INVALID_NATIONAL_ID_ERROR = ErrorCode(
        value="INVALID_NATIONAL_ID_ERROR",
        category=ErrorCategories.BUSINESS_LOGIC_ERROR,
        status_code=400,
        description="National ID is invalid.",
    )
    MISSING_PASSWORD_ERROR = ErrorCode(
        value="MISSING_PASSWORD_ERROR",
        category=ErrorCategories.BUSINESS_LOGIC_ERROR,
        status_code=400,
        description="Password is missing.",
    )
    INVALID_PASSWORD_ERROR = ErrorCode(
        value="INVALID_PASSWORD_ERROR",
        category=ErrorCategories.BUSINESS_LOGIC_ERROR,
        status_code=400,
        description="Password is invalid.",
    )
    MISSING_ROLE_ERROR = ErrorCode(
        value="MISSING_ROLE_ERROR",
        category=ErrorCategories.BUSINESS_LOGIC_ERROR,
        status_code=400,
        description="Role is missing.",
    )
    INVALID_ROLE_ERROR = ErrorCode(
        value="INVALID_ROLE_ERROR",
        category=ErrorCategories.BUSINESS_LOGIC_ERROR,
        status_code=400,
        description="Role is invalid.",
    )
    MISSING_EMAIL_ERROR = ErrorCode(
        value="MISSING_EMAIL_ERROR",
        category=ErrorCategories.BUSINESS_LOGIC_ERROR,
        status_code=400,
        description="Email is missing.",
    )
    INVALID_EMAIL_ERROR = ErrorCode(
        value="INVALID_EMAIL_ERROR",
        category=ErrorCategories.BUSINESS_LOGIC_ERROR,
        status_code=400,
        description="Email is invalid.",
    )

    # Address CRUD
    ADDRESS_NOT_FOUND_ERROR = ErrorCode(
        value="ADDRESS_NOT_FOUND_ERROR",
        category=ErrorCategories.BUSINESS_LOGIC_ERROR,
        status_code=404,
        description="Address not found.",
    )
    UPDATE_ADDRESS_ERROR = ErrorCode(
        value="UPDATE_ADDRESS_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Failed to update address.",
    )
    GET_ADDRESS_ERROR = ErrorCode(
        value="GET_ADDRESS_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Failed to retrieve address.",
    )
    GET_ADDRESS_INFO_ERROR = ErrorCode(
        value="GET_ADDRESS_INFO_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Failed to retrieve address information.",
    )
    GET_ADDRESSES_ERROR = ErrorCode(
        value="GET_ADDRESSES_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Failed to retrieve addresses.",
    )
    ADD_ADDRESS_ERROR = ErrorCode(
        value="ADD_ADDRESS_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Failed to add address.",
    )
    DELETE_ADDRESS_ERROR = ErrorCode(
        value="DELETE_ADDRESS_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Failed to delete address.",
    )
    SET_ADDRESS_AS_DEFAULT_ERROR = ErrorCode(
        value="SET_ADDRESS_AS_DEFAULT_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Failed to set address as default.",
    )
    UNSET_ADDRESS_AS_DEFAULT_ERROR = ErrorCode(
        value="UNSET_ADDRESS_AS_DEFAULT_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Failed to unset address as default.",
    )
    DEFAULT_ADDRESS_DELETION_ERROR = ErrorCode(
        value="DEFAULT_ADDRESS_DELETION_ERROR",
        category=ErrorCategories.BUSINESS_LOGIC_ERROR,
        status_code=400,
        description="Cannot delete the default address.",
    )
    ADDRESS_VALIDATION_ERROR = ErrorCode(
        value="ADDRESS_VALIDATION_ERROR",
        category=ErrorCategories.BUSINESS_LOGIC_ERROR,
        status_code=400,
        description="Address validation failed.",
    )
    ADDRESS_PERMISSION_DENIED_ERROR = ErrorCode(
        value="ADDRESS_PERMISSION_DENIED_ERROR",
        category=ErrorCategories.BUSINESS_LOGIC_ERROR,
        status_code=403,
        description="Permission denied for address operation.",
    )
    DUPLICATE_ADDRESS_ERROR = ErrorCode(
        value="DUPLICATE_ADDRESS_ERROR",
        category=ErrorCategories.BUSINESS_LOGIC_ERROR,
        status_code=409,
        description="Address already exists.",
    )
    LOAD_ADDRESS_ERROR = ErrorCode(
        value="LOAD_ADDRESS_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Failed to load address.",
    )
    BATCH_LOAD_ADDRESS_ERROR = ErrorCode(
        value="BATCH_LOAD_ADDRESS_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Failed to load addresses in batch.",
    )
    DEFAULT_ADDRESS_NOT_FOUND_ERROR = ErrorCode(
        value="DEFAULT_ADDRESS_NOT_FOUND_ERROR",
        category=ErrorCategories.BUSINESS_LOGIC_ERROR,
        status_code=404,
        description="Default address not found.",
    )

    # User CRUD Errors
    USER_REGISTRATION_ERROR = ErrorCode(
        value="USER_REGISTRATION_ERROR",
        category=ErrorCategories.BUSINESS_LOGIC_ERROR,
        status_code=400,
        description="Failed to register user.",
    )
    USER_PROFILE_UPDATE_ERROR = ErrorCode(
        value="USER_PROFILE_UPDATE_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Failed to update user profile.",
    )
    USER_LOAD_PROFILE_ERROR = ErrorCode(
        value="USER_LOAD_PROFILE_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Failed to load user profile.",
    )
    USER_LOGIN_ERROR = ErrorCode(
        value="USER_LOGIN_ERROR",
        category=ErrorCategories.BUSINESS_LOGIC_ERROR,
        status_code=400,
        description="Failed to login user.",
    )
    USER_DELETE_ACCOUNT_ERROR = ErrorCode(
        value="USER_DELETE_ACCOUNT_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Failed to delete user account.",
    )
    USER_VERIFICATION_ERROR = ErrorCode(
        value="USER_VERIFICATION_ERROR",
        category=ErrorCategories.BUSINESS_LOGIC_ERROR,
        status_code=400,
        description="User verification failed.",
    )
    USER_LOGOUT_ERROR = ErrorCode(
        value="USER_LOGOUT_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Failed to logout user.",
    )
    USER_LOAD_ACCOUNT_ERROR = ErrorCode(
        value="USER_LOAD_ACCOUNT_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Failed to load user account.",
    )
    USER_NOT_FOUND_ERROR = ErrorCode(
        value="USER_NOT_FOUND_ERROR",
        category=ErrorCategories.BUSINESS_LOGIC_ERROR,
        status_code=404,
        description="User not found.",
    )
    USER_NOT_VERIFIED_ERROR = ErrorCode(
        value="USER_NOT_VERIFIED_ERROR",
        category=ErrorCategories.BUSINESS_LOGIC_ERROR,
        status_code=400,
        description="User not verified.",
    )
    ACCOUNT_EXISTS_ERROR = ErrorCode(
        value="ACCOUNT_EXISTS_ERROR",
        category=ErrorCategories.BUSINESS_LOGIC_ERROR,
        status_code=409,
        description="Account already exists.",
    )
    INVALID_AUTHENTICATION_CODE_ERROR = ErrorCode(
        value="INVALID_AUTHENTICATION_CODE_ERROR",
        category=ErrorCategories.BUSINESS_LOGIC_ERROR,
        status_code=400,
        description="Invalid authentication code.",
    )
    LOAD_AUTHENTICATION_CODE_ERROR = ErrorCode(
        value="LOAD_AUTHENTICATION_CODE_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Failed to load authentication code.",
    )
    GENERATE_AUTHENTICATION_CODE_ERROR = ErrorCode(
        value="GENERATE_AUTHENTICATION_CODE_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Failed to generate authentication code.",
    )
    WRONG_AUTHENTICATION_CODE_ERROR = ErrorCode(
        value="WRONG_AUTHENTICATION_CODE_ERROR",
        category=ErrorCategories.BUSINESS_LOGIC_ERROR,
        status_code=400,
        description="Wrong authentication code.",
    )
    WRONG_PASSWORD_ERROR = ErrorCode(
        value="WRONG_PASSWORD_ERROR",
        category=ErrorCategories.BUSINESS_LOGIC_ERROR,
        status_code=400,
        description="Wrong password.",
    )
    RESENDING_AUTHENTICATION_CODE_ERROR = ErrorCode(
        value="RESENDING_AUTHENTICATION_CODE_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Failed to resend authentication code.",
    )
    USER_ALREADY_VERIFIED_ERROR = ErrorCode(
        value="USER_ALREADY_VERIFIED_ERROR",
        category=ErrorCategories.BUSINESS_LOGIC_ERROR,
        status_code=400,
        description="User already verified.",
    )
    USER_LOCKED_OUT_ERROR = ErrorCode(
        value="USER_LOCKED_OUT_ERROR",
        category=ErrorCategories.BUSINESS_LOGIC_ERROR,
        status_code=403,
        description="User is locked out.",
    )
    USER_SESSION_EXPIRED_ERROR = ErrorCode(
        value="USER_SESSION_EXPIRED_ERROR",
        category=ErrorCategories.BUSINESS_LOGIC_ERROR,
        status_code=403,
        description="User session has expired.",
    )
    USER_PERMISSION_DENIED_ERROR = ErrorCode(
        value="USER_PERMISSION_DENIED_ERROR",
        category=ErrorCategories.BUSINESS_LOGIC_ERROR,
        status_code=403,
        description="Permission denied for user operation.",
    )
    USER_PASSWORD_RESET_ERROR = ErrorCode(
        value="USER_PASSWORD_RESET_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Failed to reset user password.",
    )
    USER_PASSWORD_EXPIRED_ERROR = ErrorCode(
        value="USER_PASSWORD_EXPIRED_ERROR",
        category=ErrorCategories.BUSINESS_LOGIC_ERROR,
        status_code=400,
        description="User password has expired.",
    )
    USER_DUPLICATE_EMAIL_ERROR = ErrorCode(
        value="USER_DUPLICATE_EMAIL_ERROR",
        category=ErrorCategories.BUSINESS_LOGIC_ERROR,
        status_code=409,
        description="Email already exists.",
    )
    USER_EMAIL_NOT_FOUND_ERROR = ErrorCode(
        value="USER_EMAIL_NOT_FOUND_ERROR",
        category=ErrorCategories.BUSINESS_LOGIC_ERROR,
        status_code=404,
        description="Email not found.",
    )
    USER_SERVICE_UNAVAILABLE_ERROR = ErrorCode(
        value="USER_SERVICE_UNAVAILABLE_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=503,
        description="User service is unavailable.",
    )

    # DB Errors
    DB_CONNECTION_ERROR = ErrorCode(
        value="DB_CONNECTION_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Database connection error.",
    )
    DB_TRANSACTION_ERROR = ErrorCode(
        value="DB_TRANSACTION_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Database transaction error.",
    )
    DB_SESSION_CREATION_ERROR = ErrorCode(
        value="DB_SESSION_CREATION_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Database session creation error.",
    )
    DB_INSERT_ERROR = ErrorCode(
        value="DB_INSERT_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Database insert error.",
    )
    DB_FETCH_ERROR = ErrorCode(
        value="DB_FETCH_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Database fetch error.",
    )
    DB_UPDATE_ERROR = ErrorCode(
        value="DB_UPDATE_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Database update error.",
    )
    DB_JOIN_ERROR = ErrorCode(
        value="DB_JOIN_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Database join error.",
    )
    DB_DELETE_ERROR = ErrorCode(
        value="DB_DELETE_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Database delete error.",
    )
    DB_DUPLICATE_ENTRY_ERROR = ErrorCode(
        value="DB_DUPLICATE_ENTRY_ERROR",
        category=ErrorCategories.BUSINESS_LOGIC_ERROR,
        status_code=409,
        description="Duplicate database entry.",
    )
    DB_CONSTRAINT_VIOLATION_ERROR = ErrorCode(
        value="DB_CONSTRAINT_VIOLATION_ERROR",
        category=ErrorCategories.BUSINESS_LOGIC_ERROR,
        status_code=400,
        description="Database constraint violation.",
    )
    DB_TIMEOUT_ERROR = ErrorCode(
        value="DB_TIMEOUT_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Database timeout error.",
    )
    DB_INVALID_QUERY_ERROR = ErrorCode(
        value="DB_INVALID_QUERY_ERROR",
        category=ErrorCategories.BUSINESS_LOGIC_ERROR,
        status_code=400,
        description="Invalid database query.",
    )

    # Cache Errors
    CACHE_CONNECTION_ERROR = ErrorCode(
        value="CACHE_CONNECTION_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Cache connection error.",
    )
    CACHE_TRANSACTION_ERROR = ErrorCode(
        value="CACHE_TRANSACTION_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Cache transaction error.",
    )
    CACHE_SESSION_CREATION_ERROR = ErrorCode(
        value="CACHE_SESSION_CREATION_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Cache session creation error.",
    )
    CACHE_FETCH_ERROR = ErrorCode(
        value="CACHE_FETCH_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Cache fetch error.",
    )
    CACHE_INSERT_ERROR = ErrorCode(
        value="CACHE_INSERT_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Cache insert error.",
    )
    CACHE_DELETE_ERROR = ErrorCode(
        value="CACHE_DELETE_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Cache delete error.",
    )
    CACHE_EXPIRE_ERROR = ErrorCode(
        value="CACHE_EXPIRE_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Cache expire error.",
    )
    CACHE_PIPELINE_ERROR = ErrorCode(
        value="CACHE_PIPELINE_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Cache pipeline error.",
    )
    CACHE_FLUSH_ERROR = ErrorCode(
        value="CACHE_FLUSH_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Cache flush error.",
    )
    CACHE_KEY_NOT_FOUND_ERROR = ErrorCode(
        value="CACHE_KEY_NOT_FOUND_ERROR",
        category=ErrorCategories.BUSINESS_LOGIC_ERROR,
        status_code=404,
        description="Cache key not found.",
    )
    CACHE_TIMEOUT_ERROR = ErrorCode(
        value="CACHE_TIMEOUT_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Cache timeout error.",
    )
    CACHE_INVALID_COMMAND_ERROR = ErrorCode(
        value="CACHE_INVALID_COMMAND_ERROR",
        category=ErrorCategories.BUSINESS_LOGIC_ERROR,
        status_code=400,
        description="Invalid cache command.",
    )
    CACHE_AUTHENTICATION_ERROR = ErrorCode(
        value="CACHE_AUTHENTICATION_ERROR",
        category=ErrorCategories.BUSINESS_LOGIC_ERROR,
        status_code=401,
        description="Cache authentication error.",
    )

    # Message Broker Errors
    RABBITMQ_CONNECTION_ERROR = ErrorCode(
        value="RABBITMQ_CONNECTION_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="RabbitMQ connection error.",
    )
    RABBITMQ_CHANNEL_ERROR = ErrorCode(
        value="RABBITMQ_CHANNEL_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="RabbitMQ channel error.",
    )
    RABBITMQ_EXCHANGE_ERROR = ErrorCode(
        value="RABBITMQ_EXCHANGE_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="RabbitMQ exchange error.",
    )
    RABBITMQ_QUEUE_ERROR = ErrorCode(
        value="RABBITMQ_QUEUE_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="RabbitMQ queue error.",
    )
    RABBITMQ_PUBLISH_ERROR = ErrorCode(
        value="RABBITMQ_PUBLISH_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="RabbitMQ publish error.",
    )
    RABBITMQ_CONSUME_ERROR = ErrorCode(
        value="RABBITMQ_CONSUME_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="RabbitMQ consume error.",
    )
    RABBITMQ_ACK_ERROR = ErrorCode(
        value="RABBITMQ_ACK_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="RabbitMQ acknowledgment error.",
    )
    RABBITMQ_NACK_ERROR = ErrorCode(
        value="RABBITMQ_NACK_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="RabbitMQ negative acknowledgment error.",
    )
    RABBITMQ_RPC_ERROR = ErrorCode(
        value="RABBITMQ_RPC_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="RabbitMQ RPC error.",
    )
    RABBITMQ_TIMEOUT_ERROR = ErrorCode(
        value="RABBITMQ_TIMEOUT_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="RabbitMQ timeout error.",
    )
    RABBITMQ_AUTHENTICATION_ERROR = ErrorCode(
        value="RABBITMQ_AUTHENTICATION_ERROR",
        category=ErrorCategories.BUSINESS_LOGIC_ERROR,
        status_code=401,
        description="RabbitMQ authentication error.",
    )

    # Event Errors
    EVENT_CONNECTION_ERROR = ErrorCode(
        value="EVENT_CONNECTION_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Event connection error.",
    )
    EVENT_PUBLISH_ERROR = ErrorCode(
        value="EVENT_PUBLISH_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Event publish error.",
    )
    EVENT_CONSUME_ERROR = ErrorCode(
        value="EVENT_CONSUME_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Event consume error.",
    )
    EVENT_TIMEOUT_ERROR = ErrorCode(
        value="EVENT_TIMEOUT_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Event timeout error.",
    )
    EVENT_HANDLER_ERROR = ErrorCode(
        value="EVENT_HANDLER_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Event handler error.",
    )
    EVENT_ACK_ERROR = ErrorCode(
        value="EVENT_ACK_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Event acknowledgment error.",
    )
    EVENT_NACK_ERROR = ErrorCode(
        value="EVENT_NACK_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Event negative acknowledgment error.",
    )
    EVENT_PROCESSING_ERROR = ErrorCode(
        value="EVENT_PROCESSING_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Event processing error.",
    )
    EVENT_REGISTRATION_ERROR = ErrorCode(
        value="EVENT_REGISTRATION_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Event registration error.",
    )

    # API Errors
    SERVER_CONNECTION_ERROR = ErrorCode(
        value="SERVER_CONNECTION_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Server connection error.",
    )
    SERVER_TIMEOUT_ERROR = ErrorCode(
        value="SERVER_TIMEOUT_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Server timeout error.",
    )
    SERVER_AUTHENTICATION_ERROR = ErrorCode(
        value="SERVER_AUTHENTICATION_ERROR",
        category=ErrorCategories.BUSINESS_LOGIC_ERROR,
        status_code=401,
        description="Server authentication error.",
    )
    SERVER_AUTHORIZATION_ERROR = ErrorCode(
        value="SERVER_AUTHORIZATION_ERROR",
        category=ErrorCategories.BUSINESS_LOGIC_ERROR,
        status_code=403,
        description="Server authorization error.",
    )
    SERVER_NOT_FOUND_ERROR = ErrorCode(
        value="SERVER_NOT_FOUND_ERROR",
        category=ErrorCategories.BUSINESS_LOGIC_ERROR,
        status_code=404,
        description="Server not found.",
    )
    SERVER_METHOD_NOT_ALLOWED_ERROR = ErrorCode(
        value="SERVER_METHOD_NOT_ALLOWED_ERROR",
        category=ErrorCategories.BUSINESS_LOGIC_ERROR,
        status_code=405,
        description="Server method not allowed.",
    )
    SERVER_PAYLOAD_TOO_LARGE_ERROR = ErrorCode(
        value="SERVER_PAYLOAD_TOO_LARGE_ERROR",
        category=ErrorCategories.BUSINESS_LOGIC_ERROR,
        status_code=413,
        description="Server payload too large.",
    )
    SERVER_UNSUPPORTED_MEDIA_TYPE_ERROR = ErrorCode(
        value="SERVER_UNSUPPORTED_MEDIA_TYPE_ERROR",
        category=ErrorCategories.BUSINESS_LOGIC_ERROR,
        status_code=415,
        description="Server unsupported media type.",
    )
    SERVER_VALIDATION_ERROR = ErrorCode(
        value="SERVER_VALIDATION_ERROR",
        category=ErrorCategories.BUSINESS_LOGIC_ERROR,
        status_code=400,
        description="Server validation error.",
    )
    SERVER_SERVER_ERROR = ErrorCode(
        value="SERVER_SERVER_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Internal server error.",
    )
    SERVER_SERVICE_UNAVAILABLE_ERROR = ErrorCode(
        value="SERVER_SERVICE_UNAVAILABLE_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=503,
        description="Server service unavailable.",
    )
    SERVER_RATE_LIMIT_ERROR = ErrorCode(
        value="SERVER_RATE_LIMIT_ERROR",
        category=ErrorCategories.BUSINESS_LOGIC_ERROR,
        status_code=429,
        description="Server rate limit exceeded.",
    )
    MISSING_AUTHORIZATION_HEADER_ERROR = ErrorCode(
        value="MISSING_AUTHORIZATION_HEADER_ERROR",
        category=ErrorCategories.BUSINESS_LOGIC_ERROR,
        status_code=401,
        description="Missing authorization header.",
    )
    INVALID_AUTHORIZATION_HEADER_ERROR = ErrorCode(
        value="INVALID_AUTHORIZATION_HEADER_ERROR",
        category=ErrorCategories.BUSINESS_LOGIC_ERROR,
        status_code=401,
        description="Invalid authorization header.",
    )
    INVALID_AUTHORIZATION_SCHEME_ERROR = ErrorCode(
        value="INVALID_AUTHORIZATION_SCHEME_ERROR",
        category=ErrorCategories.BUSINESS_LOGIC_ERROR,
        status_code=401,
        description="Invalid authorization scheme.",
    )
    INVALID_TOKEN_ERROR = ErrorCode(
        value="INVALID_TOKEN_ERROR",
        category=ErrorCategories.BUSINESS_LOGIC_ERROR,
        status_code=401,
        description="Invalid token.",
    )
    TOKEN_NOT_FOUND_ERROR = ErrorCode(
        value="TOKEN_NOT_FOUND_ERROR",
        category=ErrorCategories.BUSINESS_LOGIC_ERROR,
        status_code=404,
        description="Token not found.",
    )
    IDENTITY_MISMATCH_ERROR = ErrorCode(
        value="IDENTITY_MISMATCH_ERROR",
        category=ErrorCategories.BUSINESS_LOGIC_ERROR,
        status_code=401,
        description="Identity mismatch.",
    )
    INTERNAL_AUTHENTICATION_ERROR = ErrorCode(
        value="INTERNAL_AUTHENTICATION_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Internal authentication error.",
    )

    # Driver Errors
    VEHICLE_SUBMISSION_ERROR = ErrorCode(
        value="VEHICLE_SUBMISSION_ERROR",
        category=ErrorCategories.BUSINESS_LOGIC_ERROR,
        status_code=400,
        description="Vehicle submission error.",
    )
    VEHICLE_GET_ERROR = ErrorCode(
        value="VEHICLE_GET_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Failed to retrieve vehicle.",
    )
    VEHICLE_REMOVE_ERROR = ErrorCode(
        value="VEHICLE_REMOVE_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Failed to remove vehicle.",
    )
    VEHICLE_MODIFY_ERROR = ErrorCode(
        value="VEHICLE_MODIFY_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Failed to modify vehicle.",
    )
    VEHICLE_NOT_FOUND_ERROR = ErrorCode(
        value="VEHICLE_NOT_FOUND_ERROR",
        category=ErrorCategories.BUSINESS_LOGIC_ERROR,
        status_code=404,
        description="Vehicle not found.",
    )
    VEHICLE_PERMISSION_DENIED_ERROR = ErrorCode(
        value="VEHICLE_PERMISSION_DENIED_ERROR",
        category=ErrorCategories.BUSINESS_LOGIC_ERROR,
        status_code=403,
        description="Permission denied for vehicle operation.",
    )
    VEHICLE_VALIDATION_ERROR = ErrorCode(
        value="VEHICLE_VALIDATION_ERROR",
        category=ErrorCategories.BUSINESS_LOGIC_ERROR,
        status_code=400,
        description="Vehicle validation failed.",
    )
    INTERNAL_SERVER_ERROR = ErrorCode(
        value="INTERNAL_SERVER_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Internal server error.",
    )
    REQUEST_TIMEOUT_ERROR = ErrorCode(
        value="REQUEST_TIMEOUT_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Request timeout error.",
    )
    REQUEST_FAILED_ERROR = ErrorCode(
        value="REQUEST_FAILED_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Request failed error.",
    )
    VEHICLE_LOAD_ERROR = ErrorCode(
        value="VEHICLE_LOAD_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Failed to load vehicle.",
    )

    # Location service
    DRIVER_STATUS_LOAD_ERROR = ErrorCode(
        value="DRIVER_STATUS_LOAD_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Failed to load driver's status.",
    )
    DRIVER_CHANGE_STATUS_ERROR = ErrorCode(
        value="DRIVER_CHANGE_STATUS_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Failed to change driver status.",
    )
    GET_NEAREST_DRIVERS_ERROR = ErrorCode(
        value="GET_NEAREST_DRIVERS_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Failed to retrieve nearest drivers.",
    )
    INVALID_LOCATION_ERROR = ErrorCode(
        value="INVALID_LOCATION_ERROR",
        category=ErrorCategories.BUSINESS_LOGIC_ERROR,
        status_code=400,
        description="Provided location is invalid.",
    )
    LOCATION_SAVE_ERROR = ErrorCode(
        value="LOCATION_SAVE_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Failed to save location.",
    )
    LOCATION_LOAD_ERROR = ErrorCode(
        value="LOCATION_LOAD_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Failed to load location.",
    )
    LOCATION_DELETE_ERROR = ErrorCode(
        value="LOCATION_DELETE_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Failed to delete location.",
    )
    LOCATION_CACHE_ERROR = ErrorCode(
        value="LOCATION_CACHE_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Location cache error.",
    )
    LOCATION_NOT_FOUND_ERROR = ErrorCode(
        value="LOCATION_NOT_FOUND_ERROR",
        category=ErrorCategories.BUSINESS_LOGIC_ERROR,
        status_code=404,
        description="Location not found.",
    )
    # Delivery Errors
    SAVE_DELIVERY_ERROR = ErrorCode(
        value="SAVE_DELIVERY_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Failed to save delivery document.",
    )
    UPDATE_DELIVERY_STATUS_ERROR = ErrorCode(
        value="UPDATE_DELIVERY_STATUS_ERROR",
        category=ErrorCategories.BUSINESS_LOGIC_ERROR,
        status_code=400,
        description="Failed to update delivery status.",
    )
    ASSIGN_DRIVER_ERROR = ErrorCode(
        value="ASSIGN_DRIVER_ERROR",
        category=ErrorCategories.BUSINESS_LOGIC_ERROR,
        status_code=400,
        description="Failed to assign driver.",
    )
    INVALID_DELIVERY_STATUS_ERROR = ErrorCode(
        value="INVALID_DELIVERY_STATUS_ERROR",
        category=ErrorCategories.BUSINESS_LOGIC_ERROR,
        status_code=400,
        description="Invalid delivery status.",
    )
    UPDATE_DELIVERY_TIMESTAMP_ERROR = ErrorCode(
        value="UPDATE_DELIVERY_TIMESTAMP_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Failed to update delivery timestamps.",
    )

    # Order Item Errors
    SAVE_ORDER_ITEM_ERROR = ErrorCode(
        value="SAVE_ORDER_ITEM_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Failed to save order item document.",
    )
    UPDATE_ORDER_ITEM_QUANTITY_ERROR = ErrorCode(
        value="UPDATE_ORDER_ITEM_QUANTITY_ERROR",
        category=ErrorCategories.BUSINESS_LOGIC_ERROR,
        status_code=400,
        description="Failed to update order item quantity.",
    )
    UPDATE_ORDER_ITEM_PRICE_ERROR = ErrorCode(
        value="UPDATE_ORDER_ITEM_PRICE_ERROR",
        category=ErrorCategories.BUSINESS_LOGIC_ERROR,
        status_code=400,
        description="Failed to update order item price.",
    )
    UPDATE_ORDER_ITEM_TIMESTAMP_ERROR = ErrorCode(
        value="UPDATE_ORDER_ITEM_TIMESTAMP_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Failed to update order item timestamps.",
    )

    # Order Status Errors
    SAVE_ORDER_STATUS_ERROR = ErrorCode(
        value="SAVE_ORDER_STATUS_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Failed to save order status document.",
    )

    # Order Errors
    SAVE_ORDER_ERROR = ErrorCode(
        value="SAVE_ORDER_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Failed to save order document.",
    )
    ADD_ORDER_ITEM_ERROR = ErrorCode(
        value="ADD_ORDER_ITEM_ERROR",
        category=ErrorCategories.BUSINESS_LOGIC_ERROR,
        status_code=400,
        description="Failed to add order item.",
    )
    REMOVE_ORDER_ITEM_ERROR = ErrorCode(
        value="REMOVE_ORDER_ITEM_ERROR",
        category=ErrorCategories.BUSINESS_LOGIC_ERROR,
        status_code=400,
        description="Failed to remove order item.",
    )
    CALCULATE_TOTAL_ERROR = ErrorCode(
        value="CALCULATE_TOTAL_ERROR",
        category=ErrorCategories.BUSINESS_LOGIC_ERROR,
        status_code=400,
        description="Failed to calculate order total.",
    )
    CHANGE_ORDER_STATUS_ERROR = ErrorCode(
        value="CHANGE_ORDER_STATUS_ERROR",
        category=ErrorCategories.BUSINESS_LOGIC_ERROR,
        status_code=400,
        description="Failed to change order status.",
    )
    PROCESS_PAYMENT_ERROR = ErrorCode(
        value="PROCESS_PAYMENT_ERROR",
        category=ErrorCategories.BUSINESS_LOGIC_ERROR,
        status_code=400,
        description="Failed to process payment.",
    )
    MARK_READY_FOR_PICKUP_ERROR = ErrorCode(
        value="MARK_READY_FOR_PICKUP_ERROR",
        category=ErrorCategories.BUSINESS_LOGIC_ERROR,
        status_code=400,
        description="Failed to mark order as ready for pickup.",
    )
    CANCEL_ORDER_ERROR = ErrorCode(
        value="CANCEL_ORDER_ERROR",
        category=ErrorCategories.BUSINESS_LOGIC_ERROR,
        status_code=400,
        description="Failed to cancel order.",
    )
    UPDATE_ORDER_TIMESTAMP_ERROR = ErrorCode(
        value="UPDATE_ORDER_TIMESTAMP_ERROR",
        category=ErrorCategories.IO_ERROR,
        status_code=500,
        description="Failed to update order timestamps.",
    )

    @classmethod
    def get_error_code(cls, error_code: str) -> ErrorCode:
        return getattr(cls, error_code.upper(), cls.UNKNOWN_ERROR)

__all__ = ["ErrorCodes", "ErrorCategories"]
