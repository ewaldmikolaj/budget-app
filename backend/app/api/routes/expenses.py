from fastapi import APIRouter
from core import crud
from ..deps import SessionDep, CurrentUserDep

router = APIRouter(prefix="/expenses")


@router.post("")
def create_expense(current_user: CurrentUserDep) -> dict:
    """Creates a new expense"""
    return {}
