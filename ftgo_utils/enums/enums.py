from enum import Enum

class Roles(Enum):
    CUSTOMER = "customer"
    ADMIN = "admin"
    RESTAURANT = "restaurant"
    DRIVER = "driver"

class Gender(Enum):
    MALE = 'male'
    FEMALE = 'female'
    UNKNOWN = 'unknown'
