from fastapi import APIRouter, HTTPException, Depends, status

from core.models import Category, CategoryCreate
from core import crud
from ..deps import SessionDep, CurrentUserDep


router = APIRouter(prefix="/categories", tags=["categories"])


@router.post("", response_model=Category)
def create_category(
    session: SessionDep, category: CategoryCreate, current_user: CurrentUserDep
) -> Category:
    """Creates a new category"""
    category = crud.create_category(session, category, current_user.id)
    if not category:
        raise HTTPException(status_code=400, detail="Bad request")

    return category


@router.get("", response_model=list[Category])
def get_categories(session: SessionDep, current_user: CurrentUserDep) -> list[Category]:
    """Get all categories"""
    categories = crud.get_categories(session, current_user.id)

    return categories
