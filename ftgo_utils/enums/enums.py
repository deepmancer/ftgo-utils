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

class ResponseStatus(Enum):
    SUCCESS = 'success'
    ERROR = 'error'

class OrderStatus(Enum):
    PENDING = 'pending'
    CONFIRMED = 'confirmed'
    CANCELLED = 'cancelled'
    DELIVERED = 'delivered'
    REJECTED = 'rejected'
    READY_FOR_DELIVERY = 'ready_for_delivery'
    IN_TRANSIT = 'in_transit'
    
class PaymentStatus(Enum):
    PENDING = 'pending'
    PAID = 'paid'
    FAILED = 'failed'
    REFUNDED = 'refunded'

class PaymentMode(Enum):
    CASH = 'cash'
    CARD = 'card'
    UPI = 'upi'
    NET_BANKING = 'net_banking'
    WALLET = 'wallet'
