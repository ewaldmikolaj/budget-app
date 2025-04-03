from sqlmodel import Field, SQLModel
from datetime import datetime


class UserBase(SQLModel):
    email: str = Field(index=True)
    password: str
    name: str
    surname: str


class User(UserBase, table=True):
    id: int = Field(default=None, primary_key=True)


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass


class UserMe(SQLModel):
    id: int
    email: str
    name: str
    surname: str
