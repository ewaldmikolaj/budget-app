from fastapi import APIRouter, HTTPException

from core.models import Expense, ExpenseCreate
from core import crud
from ..deps import SessionDep, CurrentUserDep

router = APIRouter(prefix="/expenses", tags=["expenses"])


@router.post("", response_model=Expense)
def create_expense(
    session: SessionDep, expense: ExpenseCreate, current_user: CurrentUserDep
) -> Expense:
    """Creates a new expense"""
    expense = crud.create_expense(session, expense, current_user.id)
    if not expense:
        raise HTTPException(status_code=400, detail="Bad request")

    return expense
