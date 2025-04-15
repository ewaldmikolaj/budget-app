from sqlmodel import Session, select
from typing import List

from core.models import Category, CategoryCreate, Expense


def create_category(
    session: Session, category: CategoryCreate, user_id: int
) -> Category:
    """Create a new category"""
    object = Category.model_validate(category, update={"user_id": user_id})
    session.add(object)
    session.commit()
    session.refresh(object)
    return object


def get_categories(session: Session, user_id: int) -> list[Category]:
    """Get all categories"""
    stmt = select(Category).where(Category.user_id == user_id)
    return session.exec(stmt).all()


def get_category_by_id(session: Session, category_id: int) -> Category | None:
    """Get a category by id"""
    stmt = select(Category).where(Category.id == category_id)
    return session.exec(stmt).one_or_none()


def delete_category(session: Session, category: Category) -> None:
    """Delete a category"""
    stmt = select(Expense).where(Expense.category_id == category.id)
    expenses: List[Expense] = session.exec(stmt).all()
    for expense in expenses:
        expense.category_id = None
    session.commit()

    session.delete(category)
    session.commit()
    return None
