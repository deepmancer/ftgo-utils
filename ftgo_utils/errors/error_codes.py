
from .data_structures import ErrorCode, ErrorCategory

class ErrorCodes:
    UNKNOWN_ERROR = ErrorCode(
        id="UNKNOWN_ERROR",
        category=ErrorCategory.GENERIC_ERROR,
    )
    # Field Validation Errors
    MISSING_PHONE_NUMBER_ERROR = ErrorCode(
        id="MISSING_PHONE_NUMBER_ERROR",
        category=ErrorCategory.VALIDATION_ERROR,
    )
    INVALID_PHONE_NUMBER_ERROR = ErrorCode(
        id="INVALID_PHONE_NUMBER_ERROR",
        category=ErrorCategory.VALIDATION_ERROR,
    )
    MISSING_NATIONAL_ID_ERROR = ErrorCode(
        id="MISSING_NATIONAL_ID_ERROR",
        category=ErrorCategory.VALIDATION_ERROR,
    )
    INVALID_NATIONAL_ID_ERROR = ErrorCode(
        id="INVALID_NATIONAL_ID_ERROR",
        category=ErrorCategory.VALIDATION_ERROR,
    )
    MISSING_PASSWORD_ERROR = ErrorCode(
        id="MISSING_PASSWORD_ERROR",
        category=ErrorCategory.VALIDATION_ERROR,
    )
    INVALID_PASSWORD_ERROR = ErrorCode(
        id="INVALID_PASSWORD_ERROR",
        category=ErrorCategory.VALIDATION_ERROR,
    )
    MISSING_ROLE_ERROR = ErrorCode(
        id="MISSING_ROLE_ERROR",
        category=ErrorCategory.VALIDATION_ERROR,
    )
    INVALID_ROLE_ERROR = ErrorCode(
        id="INVALID_ROLE_ERROR",
        category=ErrorCategory.VALIDATION_ERROR,
    )
    MISSING_EMAIL_ERROR = ErrorCode(
        id="MISSING_EMAIL_ERROR",
        category=ErrorCategory.VALIDATION_ERROR,
    )
    INVALID_EMAIL_ERROR = ErrorCode(
        id="INVALID_EMAIL_ERROR",
        category=ErrorCategory.VALIDATION_ERROR,
    )

    # Address CRUD
    ADDRESS_NOT_FOUND_ERROR = ErrorCode(
        id="ADDRESS_NOT_FOUND_ERROR",
        category=ErrorCategory.DOMAIN_ERROR,
    )
    UPDATE_ADDRESS_ERROR = ErrorCode(
        id="UPDATE_ADDRESS_ERROR",
        category=ErrorCategory.DOMAIN_ERROR,
    )
    GET_ADDRESS_ERROR = ErrorCode(
        id="GET_ADDRESS_ERROR",
        category=ErrorCategory.DOMAIN_ERROR,
    )
    GET_ADDRESS_INFO_ERROR = ErrorCode(
        id="GET_ADDRESS_INFO_ERROR",
        category=ErrorCategory.DOMAIN_ERROR,
    )
    GET_ADDRESSES_ERROR = ErrorCode(
        id="GET_ADDRESSES_ERROR",
        category=ErrorCategory.DOMAIN_ERROR,
    )
    ADD_ADDRESS_ERROR = ErrorCode(
        id="ADD_ADDRESS_ERROR",
        category=ErrorCategory.DOMAIN_ERROR,
    )
    DELETE_ADDRESS_ERROR = ErrorCode(
        id="DELETE_ADDRESS_ERROR",
        category=ErrorCategory.DOMAIN_ERROR,
    )
    SET_ADDRESS_AS_DEFAULT_ERROR = ErrorCode(
        id="SET_ADDRESS_AS_DEFAULT_ERROR",
        category=ErrorCategory.DOMAIN_ERROR,
    )
    UNSET_ADDRESS_AS_DEFAULT_ERROR = ErrorCode(
        id="UNSET_ADDRESS_AS_DEFAULT_ERROR",
        category=ErrorCategory.DOMAIN_ERROR,
    )
    DEFAULT_ADDRESS_DELETION_ERROR = ErrorCode(
        id="DEFAULT_ADDRESS_DELETION_ERROR",
        category=ErrorCategory.DOMAIN_ERROR,
    )
    ADDRESS_VALIDATION_ERROR = ErrorCode(
        id="ADDRESS_VALIDATION_ERROR",
        category=ErrorCategory.VALIDATION_ERROR,
    )
    ADDRESS_PERMISSION_DENIED_ERROR = ErrorCode(
        id="ADDRESS_PERMISSION_DENIED_ERROR",
        category=ErrorCategory.DOMAIN_ERROR,
    )
    DUPLICATE_ADDRESS_ERROR = ErrorCode(
        id="DUPLICATE_ADDRESS_ERROR",
        category=ErrorCategory.DOMAIN_ERROR,
    )
    LOAD_ADDRESS_ERROR = ErrorCode(
        id="LOAD_ADDRESS_ERROR",
        category=ErrorCategory.DOMAIN_ERROR,
    )
    BATCH_LOAD_ADDRESS_ERROR = ErrorCode(
        id="BATCH_LOAD_ADDRESS_ERROR",
        category=ErrorCategory.DOMAIN_ERROR,
    )
    DEFAULT_ADDRESS_NOT_FOUND_ERROR = ErrorCode(
        id="DEFAULT_ADDRESS_NOT_FOUND_ERROR",
        category=ErrorCategory.DOMAIN_ERROR,
    )

    # User CRUD Errors
    USER_REGISTRATION_ERROR = ErrorCode(
        id="USER_REGISTRATION_ERROR",
        category=ErrorCategory.DOMAIN_ERROR,
    )
    USER_PROFILE_UPDATE_ERROR = ErrorCode(
        id="USER_PROFILE_UPDATE_ERROR",
        category=ErrorCategory.DOMAIN_ERROR,
    )
    USER_LOGIN_ERROR = ErrorCode(
        id="USER_LOGIN_ERROR",
        category=ErrorCategory.DOMAIN_ERROR,
    )
    USER_DELETE_ACCOUNT_ERROR = ErrorCode(
        id="USER_DELETE_ACCOUNT_ERROR",
        category=ErrorCategory.DOMAIN_ERROR,
    )
    USER_VERIFICATION_ERROR = ErrorCode(
        id="USER_VERIFICATION_ERROR",
        category=ErrorCategory.DOMAIN_ERROR,
    )
    USER_LOGOUT_ERROR = ErrorCode(
        id="USER_LOGOUT_ERROR",
        category=ErrorCategory.DOMAIN_ERROR,
    )
    USER_LOAD_ACCOUNT_ERROR = ErrorCode(
        id="USER_LOAD_ACCOUNT_ERROR",
        category=ErrorCategory.DOMAIN_ERROR,
    )
    USER_NOT_FOUND_ERROR = ErrorCode(
        id="USER_NOT_FOUND_ERROR",
        category=ErrorCategory.DOMAIN_ERROR,
    )
    USER_NOT_VERIFIED_ERROR = ErrorCode(
        id="USER_NOT_VERIFIED_ERROR",
        category=ErrorCategory.DOMAIN_ERROR,
    )
    ACCOUNT_EXISTS_ERROR = ErrorCode(
        id="ACCOUNT_EXISTS_ERROR",
        category=ErrorCategory.DOMAIN_ERROR,
    )
    INVALID_AUTHENTICATION_CODE_ERROR = ErrorCode(
        id="INVALID_AUTHENTICATION_CODE_ERROR",
        category=ErrorCategory.DOMAIN_ERROR,
    )
    WRONG_AUTHENTICATION_CODE_ERROR = ErrorCode(
        id="WRONG_AUTHENTICATION_CODE_ERROR",
        category=ErrorCategory.DOMAIN_ERROR,
    )
    WRONG_PASSWORD_ERROR = ErrorCode(
        id="WRONG_PASSWORD_ERROR",
        category=ErrorCategory.DOMAIN_ERROR,
    )
    RESENDING_AUTHENTICATION_CODE_ERROR = ErrorCode(
        id="RESENDING_AUTHENTICATION_CODE_ERROR",
        category=ErrorCategory.SERVER_ERROR,
    )
    USER_ALREADY_VERIFIED_ERROR = ErrorCode(
        id="USER_ALREADY_VERIFIED_ERROR",
        category=ErrorCategory.DOMAIN_ERROR,
    )
    USER_LOCKED_OUT_ERROR = ErrorCode(
        id="USER_LOCKED_OUT_ERROR",
        category=ErrorCategory.DOMAIN_ERROR,
    )
    USER_SESSION_EXPIRED_ERROR = ErrorCode(
        id="USER_SESSION_EXPIRED_ERROR",
        category=ErrorCategory.DOMAIN_ERROR,
    )
    USER_PERMISSION_DENIED_ERROR = ErrorCode(
        id="USER_PERMISSION_DENIED_ERROR",
        category=ErrorCategory.DOMAIN_ERROR,
    )
    USER_PASSWORD_RESET_ERROR = ErrorCode(
        id="USER_PASSWORD_RESET_ERROR",
        category=ErrorCategory.DOMAIN_ERROR,
    )
    USER_PASSWORD_EXPIRED_ERROR = ErrorCode(
        id="USER_PASSWORD_EXPIRED_ERROR",
        category=ErrorCategory.DOMAIN_ERROR,
    )
    USER_DUPLICATE_EMAIL_ERROR = ErrorCode(
        id="USER_DUPLICATE_EMAIL_ERROR",
        category=ErrorCategory.DOMAIN_ERROR,
    )
    USER_EMAIL_NOT_FOUND_ERROR = ErrorCode(
        id="USER_EMAIL_NOT_FOUND_ERROR",
        category=ErrorCategory.DOMAIN_ERROR,
    )
    USER_SERVICE_UNAVAILABLE_ERROR = ErrorCode(
        id="USER_SERVICE_UNAVAILABLE_ERROR",
        category=ErrorCategory.MESSAGE_BROKER_ERROR,
    )

    # DB Errors
    DB_CONNECTION_ERROR = ErrorCode(
        id="DB_CONNECTION_ERROR",
        category=ErrorCategory.CONNECTION_ERROR,
    )
    DB_TRANSACTION_ERROR = ErrorCode(
        id="DB_TRANSACTION_ERROR",
        category=ErrorCategory.DATABASE_ERROR,
    )
    DB_SESSION_CREATION_ERROR = ErrorCode(
        id="DB_SESSION_CREATION_ERROR",
        category=ErrorCategory.DATABASE_ERROR,
    )
    DB_INSERT_ERROR = ErrorCode(
        id="DB_INSERT_ERROR",
        category=ErrorCategory.DATABASE_ERROR,
    )
    DB_FETCH_ERROR = ErrorCode(
        id="DB_FETCH_ERROR",
        category=ErrorCategory.DATABASE_ERROR,
    )
    DB_UPDATE_ERROR = ErrorCode(
        id="DB_UPDATE_ERROR",
        category=ErrorCategory.DATABASE_ERROR,
    )
    DB_JOIN_ERROR = ErrorCode(
        id="DB_JOIN_ERROR",
        category=ErrorCategory.DATABASE_ERROR,
    )
    DB_DELETE_ERROR = ErrorCode(
        id="DB_DELETE_ERROR",
        category=ErrorCategory.DATABASE_ERROR,
    )
    DB_DUPLICATE_ENTRY_ERROR = ErrorCode(
        id="DB_DUPLICATE_ENTRY_ERROR",
        category=ErrorCategory.DATABASE_ERROR,
    )
    DB_CONSTRAINT_VIOLATION_ERROR = ErrorCode(
        id="DB_CONSTRAINT_VIOLATION_ERROR",
        category=ErrorCategory.DATABASE_ERROR,
    )
    DB_TIMEOUT_ERROR = ErrorCode(
        id="DB_TIMEOUT_ERROR",
        category=ErrorCategory.DATABASE_ERROR,
    )
    DB_INVALID_QUERY_ERROR = ErrorCode(
        id="DB_INVALID_QUERY_ERROR",
        category=ErrorCategory.DATABASE_ERROR,
    )

    # Cache Errors
    CACHE_CONNECTION_ERROR = ErrorCode(
        id="CACHE_CONNECTION_ERROR",
        category=ErrorCategory.CONNECTION_ERROR,
    )
    CACHE_TRANSACTION_ERROR = ErrorCode(
        id="CACHE_TRANSACTION_ERROR",
        category=ErrorCategory.CACHE_ERROR,
    )
    CACHE_SESSION_CREATION_ERROR = ErrorCode(
        id="CACHE_SESSION_CREATION_ERROR",
        category=ErrorCategory.CACHE_ERROR,
    )
    CACHE_FETCH_ERROR = ErrorCode(
        id="CACHE_FETCH_ERROR",
        category=ErrorCategory.CACHE_ERROR,
    )
    CACHE_INSERT_ERROR = ErrorCode(
        id="CACHE_INSERT_ERROR",
        category=ErrorCategory.CACHE_ERROR,
    )
    CACHE_DELETE_ERROR = ErrorCode(
        id="CACHE_DELETE_ERROR",
        category=ErrorCategory.CACHE_ERROR,
    )
    CACHE_EXPIRE_ERROR = ErrorCode(
        id="CACHE_EXPIRE_ERROR",
        category=ErrorCategory.CACHE_ERROR,
    )
    CACHE_PIPELINE_ERROR = ErrorCode(
        id="CACHE_PIPELINE_ERROR",
        category=ErrorCategory.CACHE_ERROR,
    )
    CACHE_FLUSH_ERROR = ErrorCode(
        id="CACHE_FLUSH_ERROR",
        category=ErrorCategory.CACHE_ERROR,
    )
    CACHE_KEY_NOT_FOUND_ERROR = ErrorCode(
        id="CACHE_KEY_NOT_FOUND_ERROR",
        category=ErrorCategory.CACHE_ERROR,
    )
    CACHE_TIMEOUT_ERROR = ErrorCode(
        id="CACHE_TIMEOUT_ERROR",
        category=ErrorCategory.CACHE_ERROR,
    )
    CACHE_INVALID_COMMAND_ERROR = ErrorCode(
        id="CACHE_INVALID_COMMAND_ERROR",
        category=ErrorCategory.CACHE_ERROR,
    )
    CACHE_AUTHENTICATION_ERROR = ErrorCode(
        id="CACHE_AUTHENTICATION_ERROR",
        category=ErrorCategory.CACHE_ERROR,
    )

    # Message Broker Errors
    RABBITMQ_CONNECTION_ERROR = ErrorCode(
        id="RABBITMQ_CONNECTION_ERROR",
        category=ErrorCategory.CONNECTION_ERROR,
    )
    RABBITMQ_CHANNEL_ERROR = ErrorCode(
        id="RABBITMQ_CHANNEL_ERROR",
        category=ErrorCategory.RABBITMQ_ERROR,
    )
    RABBITMQ_EXCHANGE_ERROR = ErrorCode(
        id="RABBITMQ_EXCHANGE_ERROR",
        category=ErrorCategory.RABBITMQ_ERROR,
    )
    RABBITMQ_QUEUE_ERROR = ErrorCode(
        id="RABBITMQ_QUEUE_ERROR",
        category=ErrorCategory.RABBITMQ_ERROR,
    )
    RABBITMQ_PUBLISH_ERROR = ErrorCode(
        id="RABBITMQ_PUBLISH_ERROR",
        category=ErrorCategory.RABBITMQ_ERROR,
    )
    RABBITMQ_CONSUME_ERROR = ErrorCode(
        id="RABBITMQ_CONSUME_ERROR",
        category=ErrorCategory.RABBITMQ_ERROR,
    )
    RABBITMQ_ACK_ERROR = ErrorCode(
        id="RABBITMQ_ACK_ERROR",
        category=ErrorCategory.RABBITMQ_ERROR,
    )
    RABBITMQ_NACK_ERROR = ErrorCode(
        id="RABBITMQ_NACK_ERROR",
        category=ErrorCategory.RABBITMQ_ERROR,
    )
    RABBITMQ_RPC_ERROR = ErrorCode(
        id="RABBITMQ_RPC_ERROR",
        category=ErrorCategory.RABBITMQ_ERROR,
    )
    RABBITMQ_TIMEOUT_ERROR = ErrorCode(
        id="RABBITMQ_TIMEOUT_ERROR",
        category=ErrorCategory.RABBITMQ_ERROR,
    )
    RABBITMQ_AUTHENTICATION_ERROR = ErrorCode(
        id="RABBITMQ_AUTHENTICATION_ERROR",
        category=ErrorCategory.RABBITMQ_ERROR,
    )

    # Event Errors
    EVENT_CONNECTION_ERROR = ErrorCode(
        id="EVENT_CONNECTION_ERROR",
        category=ErrorCategory.NETWORK_ERROR,
    )
    EVENT_PUBLISH_ERROR = ErrorCode(
        id="EVENT_PUBLISH_ERROR",
        category=ErrorCategory.MESSAGE_BROKER_ERROR,
    )
    EVENT_CONSUME_ERROR = ErrorCode(
        id="EVENT_CONSUME_ERROR",
        category=ErrorCategory.MESSAGE_BROKER_ERROR,
    )
    EVENT_TIMEOUT_ERROR = ErrorCode(
        id="EVENT_TIMEOUT_ERROR",
        category=ErrorCategory.MESSAGE_BROKER_ERROR,
    )
    EVENT_HANDLER_ERROR = ErrorCode(
        id="EVENT_HANDLER_ERROR",
        category=ErrorCategory.MESSAGE_BROKER_ERROR,
    )
    EVENT_ACK_ERROR = ErrorCode(
        id="EVENT_ACK_ERROR",
        category=ErrorCategory.MESSAGE_BROKER_ERROR,
    )
    EVENT_NACK_ERROR = ErrorCode(
        id="EVENT_NACK_ERROR",
        category=ErrorCategory.MESSAGE_BROKER_ERROR,
    )
    EVENT_PROCESSING_ERROR = ErrorCode(
        id="EVENT_PROCESSING_ERROR",
        category=ErrorCategory.MESSAGE_BROKER_ERROR,
    )
    EVENT_REGISTERATION_ERROR = ErrorCode(
        id="EVENT_REGISTERATION_ERROR",
        category=ErrorCategory.MESSAGE_BROKER_ERROR,
    )

    # API Errors
    API_CONNECTION_ERROR = ErrorCode(
        id="API_CONNECTION_ERROR",
        category=ErrorCategory.NETWORK_ERROR,
    )
    API_TIMEOUT_ERROR = ErrorCode(
        id="API_TIMEOUT_ERROR",
        category=ErrorCategory.NETWORK_ERROR,
    )
    API_AUTHENTICATION_ERROR = ErrorCode(
        id="API_AUTHENTICATION_ERROR",
        category=ErrorCategory.SERVER_ERROR,
    )
    API_AUTHORIZATION_ERROR = ErrorCode(
        id="API_AUTHORIZATION_ERROR",
        category=ErrorCategory.SERVER_ERROR,
    )
    API_NOT_FOUND_ERROR = ErrorCode(
        id="API_NOT_FOUND_ERROR",
        category=ErrorCategory.SERVER_ERROR,
    )
    API_METHOD_NOT_ALLOWED_ERROR = ErrorCode(
        id="API_METHOD_NOT_ALLOWED_ERROR",
        category=ErrorCategory.SERVER_ERROR,
    )
    API_PAYLOAD_TOO_LARGE_ERROR = ErrorCode(
        id="API_PAYLOAD_TOO_LARGE_ERROR",
        category=ErrorCategory.SERVER_ERROR,
    )
    API_UNSUPPORTED_MEDIA_TYPE_ERROR = ErrorCode(
        id="API_UNSUPPORTED_MEDIA_TYPE_ERROR",
        category=ErrorCategory.SERVER_ERROR,
    )
    API_VALIDATION_ERROR = ErrorCode(
        id="API_VALIDATION_ERROR",
        category=ErrorCategory.VALIDATION_ERROR,
    )
    API_SERVER_ERROR = ErrorCode(
        id="API_SERVER_ERROR",
        category=ErrorCategory.SERVER_ERROR,
    )
    API_SERVICE_UNAVAILABLE_ERROR = ErrorCode(
        id="API_SERVICE_UNAVAILABLE_ERROR",
        category=ErrorCategory.SERVER_ERROR,
    )
    API_RATE_LIMIT_ERROR = ErrorCode(
        id="API_RATE_LIMIT_ERROR",
        category=ErrorCategory.SERVER_ERROR,
    )

    # Driver Errors
    VEHICLE_SUBMISSION_ERROR = ErrorCode(
        id="VEHICLE_SUBMISSION_ERROR",
        category=ErrorCategory.DOMAIN_ERROR,
    )
    VEHICLE_GET_ERROR = ErrorCode(
        id="VEHICLE_GET_ERROR",
        category=ErrorCategory.DOMAIN_ERROR,
    )
    VEHICLE_REMOVE_ERROR = ErrorCode(
        id="VEHICLE_REMOVE_ERROR",
        category=ErrorCategory.DOMAIN_ERROR,
    )
    VEHICLE_MODIFY_ERROR = ErrorCode(
        id="VEHICLE_MODIFY_ERROR",
        category=ErrorCategory.DOMAIN_ERROR,
    )
    VEHICLE_NOT_FOUND_ERROR = ErrorCode(
        id="VEHICLE_NOT_FOUND_ERROR",
        category=ErrorCategory.DOMAIN_ERROR,
    )
    VEHICLE_PERMISSION_DENIED_ERROR = ErrorCode(
        id="VEHICLE_PERMISSION_DENIED_ERROR",
        category=ErrorCategory.DOMAIN_ERROR,
    )
    VEHICLE_VALIDATION_ERROR = ErrorCode(
        id="VEHICLE_VALIDATION_ERROR",
        category=ErrorCategory.VALIDATION_ERROR,
    )
    
__all__ = ["ErrorCodes"]
