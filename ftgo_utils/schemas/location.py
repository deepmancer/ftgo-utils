from pydantic import Field

from .base import BaseModel as BaseSchema
from .fields import LocationPointMixin

class LocationMixin(LocationPointMixin):
    timestamp: float = Field(..., ge=0)
    accuracy: Optional[float] = Field(None, ge=0)
    speed: Optional[float] = Field(None, ge=0)
    bearing: Optional[float] = Field(None, ge=0, le=360)
    altitude: Optional[float] = Field(None, ge=0)
