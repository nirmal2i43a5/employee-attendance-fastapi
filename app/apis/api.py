from fastapi import APIRouter

from app.apis.routers import user,login

api_router = APIRouter()

api_router.include_router(user.router, prefix="/users", tags=["users"])
api_router.include_router(login.router, prefix="/login", tags=["authentication"])