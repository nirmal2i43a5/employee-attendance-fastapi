
from pydantic import BaseModel, Optional, EmailStr
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
class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True



# Additional properties to return via API
class User(UserInDBBase):
    pass


# Additional properties stored in DB
class UserInDB(UserInDBBase):
    hashed_password: str

