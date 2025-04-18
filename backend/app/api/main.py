from fastapi import APIRouter

from .routes import auth, users, expenses, categories, incomes


api_router = APIRouter()
api_router.include_router(users.router)
api_router.include_router(auth.router)
api_router.include_router(expenses.router)
api_router.include_router(categories.router)
api_router.include_router(incomes.router)
