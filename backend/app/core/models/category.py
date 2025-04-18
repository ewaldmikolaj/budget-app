from sqlmodel import Field, SQLModel


class CategoryBase(SQLModel):
    name: str = Field(max_length=100, unique=True)


class Category(CategoryBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    user_id: int | None = Field(default=None, foreign_key="user.id")


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(CategoryBase):
    pass
