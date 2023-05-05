from app import  models, schemas
from typing import List
from fastapi import APIRouter,HTTPException,Depends
from fastapi.responses import JSONResponse
from app.db import SessionLocal
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import (
    UserRead,UserCreate,UserUpdate
)
from app.db import get_db
from app.core.security import get_password_hash

router = APIRouter()


@router.post("/create/", response_model = User)
def create_user(user: UserCreate,  db: Session = Depends(get_db)):

    user = db.query(User).filter(email = user.email)

    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )
    db_obj = User(
            full_name=user.full_name,

            email=user.email,
            hashed_password=get_password_hash(user.password),
            is_superuser=user.is_superuser,
        )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return JSONResponse(content={"message": "User created successfully"})
   








    user = crud.user.get_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )
    user = crud.user.create(db, obj_in=user_in)
    if settings.EMAILS_ENABLED and user_in.email:
        send_new_account_email(
            email_to=user_in.email, username=user_in.email, password=user_in.password
        )
    return user
