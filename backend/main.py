from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlmodel import SQLModel, Session, create_engine

from core.models import Budget, Category, Expense, Income, Notification, User


@asynccontextmanager
async def lifespan(app: FastAPI):
    engine = create_engine("postgresql+psycopg2://admin:admin@localhost/budget_db")
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session

app = FastAPI(lifespan=lifespan)