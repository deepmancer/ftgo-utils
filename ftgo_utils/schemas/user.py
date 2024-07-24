
from typing import Optional
from pydantic import Field, EmailStr

from .base import BaseModel as BaseSchema
from .fields import PhoneNumberMixin, RoleMixin, GenderMixin, NationalIdMixin, uuid_field

class UserInfoMixin(PhoneNumberMixin, RoleMixin, GenderMixin, NationalIdMixin):
    first_name: str = Field(..., min_length=1, max_length=50)
    last_name: str = Field(..., min_length=1, max_length=50)
    email: Optional[EmailStr] = Field(None, min_length=1, max_length=100)

class UserMixin(UserInfoMixin):
    user_id: str = uuid_field()
