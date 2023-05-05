from fastapi import APIRouter

from app.apis.routers import user

api_router = APIRouter()

api_router.include_router(user.router, prefix="/users", tags=["users"])