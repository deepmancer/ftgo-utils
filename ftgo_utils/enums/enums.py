from enum import Enum

class Roles(str, Enum):
    CUSTOMER = "customer"
    ADMIN = "admin"
    RESTAURANT_ADMIN = "restaurant_admin"
    DRIVER = "driver"
    STAFF = "staff"

class Gender(str, Enum):
    MALE = 'male'
    FEMALE = 'female'
    UNKNOWN = 'unknown'

class ResponseStatus(str, Enum):
    SUCCESS = 'success'
    FAILURE = 'failure'
    ERROR = 'error'

class OrderStatus(str, Enum):
    PENDING = 'pending'
    CONFIRMED = 'confirmed'
    CANCELLED = 'cancelled'
    READY_FOR_PICKUP = 'ready_for_pickup'
    OUT_FOR_DELIVERY = 'out_for_delivery'
    DELIVERED = 'delivered'
    REJECTED = 'rejected'

class DeliveryStatus(str, Enum):
    PENDING = 'pending'
    ASSIGNED = 'assigned'
    PICKED_UP = 'picked_up'
    DELIVERED = 'delivered'
    CANCELLED = 'cancelled'

class PaymentStatus(str, Enum):
    PENDING = 'pending'
    PAID = 'paid'
    FAILED = 'failed'
    REFUNDED = 'refunded'

class DriverStatus(str, Enum):
    ONLINE = 'online'
    OFFLINE = 'offline'
    
class DriverAvailabilityStatus(str, Enum):
    AVAILABLE = 'available'
    OCCUPIED = 'occupied'

class Languages(str, Enum):
    EN = 'en'
    FA = 'fa'
