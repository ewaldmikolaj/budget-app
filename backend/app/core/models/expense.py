from sqlmodel import Field, SQLModel
from datetime import datetime
from decimal import Decimal


class ExpenseBase(SQLModel):
    summary: str = Field(max_length=100)
    amount: Decimal = Field(decimal_places=2)
    transaction_date: datetime = Field(default_factory=lambda: datetime.now())

    category_id: int | None = Field(default=None, foreign_key="category.id")


class Expense(ExpenseBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    user_id: int | None = Field(default=None, foreign_key="user.id")


class ExpenseCreate(ExpenseBase):
    pass


class ExpenseUpdate(ExpenseBase):
    pass
