from enum import Enum

class Roles(Enum):
    CUSTOMER = "customer"
    ADMIN = "admin"
    RESTAURANT_ADMIN = "restaurant_admin"
    DRIVER = "driver"
    STAFF = "staff"

class Gender(Enum):
    MALE = 'male'
    FEMALE = 'female'
    UNKNOWN = 'unknown'
