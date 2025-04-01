from fastapi import APIRouter

from .routes import auth, users, expenses


api_router = APIRouter()
api_router.include_router(users.router)
api_router.include_router(auth.router)
api_router.include_router(expenses.router)
