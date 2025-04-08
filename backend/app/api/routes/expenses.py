from fastapi import APIRouter, HTTPException

from core.models import Expense, ExpenseCreate, ExpenseWithCategory
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


@router.get("", response_model=list[ExpenseWithCategory])
def get_expenses(
    session: SessionDep, current_user: CurrentUserDep
) -> list[ExpenseWithCategory]:
    """Get all expenses"""
    expenses = crud.get_expenses(session, current_user.id)

    return expenses
