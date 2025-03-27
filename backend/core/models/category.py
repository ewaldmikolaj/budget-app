from sqlmodel import Field, SQLModel

class Category(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(max_length=100)
    
    user_id: int | None = Field(default=None, foreign_key="user.id")