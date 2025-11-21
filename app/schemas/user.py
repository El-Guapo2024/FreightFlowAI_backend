from pydantic import BaseModel
from .base import AppBaseModel

class UserBase(AppBaseModel):
    name: str
    role: str = "driver"

class UserCreate(UserBase):
    pass # will add later

class UserOut(UserBase):
    id: int