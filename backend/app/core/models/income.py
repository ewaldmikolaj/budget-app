from sqlmodel import Field, SQLModel
from datetime import datetime

class Income(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    summary: str = Field(max_length=100)
    amount: float = Field(decimal_places=2)
    transaction_date: datetime = Field(default_factory=lambda: datetime.now())
    source: str = Field(max_length=200)

    user_id: int | None = Field(default=None, foreign_key="user.id")