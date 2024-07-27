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
    DELIVERED = 'delivered'
    REJECTED = 'rejected'
    READY_FOR_DELIVERY = 'ready_for_delivery'
    IN_TRANSIT = 'in_transit'
    
class PaymentStatus(str, Enum):
    PENDING = 'pending'
    PAID = 'paid'
    FAILED = 'failed'
    REFUNDED = 'refunded'

class PaymentMode(str, Enum):
    CASH = 'cash'
    CARD = 'card'
    UPI = 'upi'
    NET_BANKING = 'net_banking'
    WALLET = 'wallet'

class DriverStatus(str, Enum):
    ONLINE = 'online'
    OFFLINE = 'offline'
    
class DriverAvailabilityStatus(str, Enum):
    AVAILABLE = 'available'
    OCCUPIED = 'occupied'
