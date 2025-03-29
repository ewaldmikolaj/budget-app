from fastapi import APIRouter

from .routes import users
from .routes import auth


api_router = APIRouter()
api_router.include_router(users.router)
api_router.include_router(auth.router)
