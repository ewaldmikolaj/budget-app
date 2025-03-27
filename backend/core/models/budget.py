from sqlmodel import Field, SQLModel

class Budget(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    amount: float = Field(decimal_places=2)
    period: str
    status: str

    user_id: int | None = Field(default=None, foreign_key="user.id")