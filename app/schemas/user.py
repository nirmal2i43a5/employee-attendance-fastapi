
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

# Shared properties
class UserBase(BaseModel):
    full_name: Optional[str] = None
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True
    is_superuser: bool = False


class UserCreate(UserBase):
    email: EmailStr
    password: str


class UserUpdate(UserBase):
    password: Optional[str] = None


# fetching all users
class UserRead(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class User(UserRead):
    pass


# Additional properties stored in DB
class UserInDB(UserRead):
    hashed_password: str

