from sqlmodel import Field, SQLModel

class Notification(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    threshold: int
    status: str

    budget_id: int | None = Field(default=None, foreign_key="budget.id")
    user_id: int | None = Field(default=None, foreign_key="user.id")