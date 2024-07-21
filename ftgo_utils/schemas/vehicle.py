from pydantic import Field

from .base import BaseModel as BaseSchema
from .fields import uuid_field

class VehicleInfoMixin(BaseSchema):
    plate_number: str = Field(..., min_length=1, max_length=20)
    license_number: str = Field(..., min_length=1, max_length=20)

class VehicleMixin(VehicleInfoMixin):
    vehicle_id: str = uuid_field()
    driver_id: str = uuid_field()
