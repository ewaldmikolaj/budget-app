from sqlmodel import Session, select

from core.models import Category, CategoryCreate


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
