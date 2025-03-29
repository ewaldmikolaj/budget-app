from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlmodel import SQLModel

from core.models import Budget, Category, Expense, Income, Notification, User
from core.db import engine
from api.main import api_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(api_router)