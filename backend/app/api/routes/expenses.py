from fastapi import APIRouter, HTTPException, status

from core.models import Expense, ExpenseCreate, ExpenseGet
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


@router.get("", response_model=list[ExpenseGet])
def get_expenses(session: SessionDep, current_user: CurrentUserDep) -> list[ExpenseGet]:
    """Get all expenses"""
    expenses = crud.get_expenses(session, current_user.id)

    return expenses


@router.delete("/{expense_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_expense(
    session: SessionDep,
    expense_id: int,
    current_user: CurrentUserDep,
) -> None:
    """Delete an expense"""
    expense: Expense = crud.get_expense_by_id(session, expense_id)
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")

    if expense.user_id != current_user.id:
        raise HTTPException(
            status_code=403, detail="Not authorized to delete this expense"
        )

    crud.delete_expense(session, expense)
    return None
