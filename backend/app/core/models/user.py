from sqlmodel import Field, SQLModel
from datetime import datetime

class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    email: str
    password: str
    name: str
    surname: str