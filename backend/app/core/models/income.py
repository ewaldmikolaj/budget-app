from sqlmodel import Field, SQLModel
from datetime import datetime
from decimal import Decimal


class IncomeBase(SQLModel):
    summary: str = Field(max_length=100)
    amount: Decimal = Field(decimal_places=2)
    transaction_date: datetime = Field(default_factory=lambda: datetime.now())
    source: str = Field(max_length=200)


class Income(IncomeBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    user_id: int | None = Field(default=None, foreign_key="user.id")


class IncomeCreate(IncomeBase):
    pass


class IncomeUpdate(IncomeBase):
    pass


class IncomeGet(IncomeBase):
    id: int
