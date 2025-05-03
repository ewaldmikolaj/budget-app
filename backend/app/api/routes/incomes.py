from fastapi import APIRouter, HTTPException, status

from core.models import Income, IncomeCreate, IncomeGet
from core import crud
from ..deps import SessionDep, CurrentUserDep

router = APIRouter(prefix="/incomes", tags=["incomes"])


@router.post("", response_model=Income)
def create_income(
    session: SessionDep, income: IncomeCreate, current_user: CurrentUserDep
) -> Income:
    """Creates a new income"""
    income = crud.create_income(session, income, current_user.id)
    if not income:
        raise HTTPException(status_code=400, detail="Bad request")

    return income


@router.get("", response_model=list[IncomeGet])
def get_incomes(session: SessionDep, current_user: CurrentUserDep) -> list[IncomeGet]:
    """Get all incomes"""
    incomes = crud.get_incomes(session, current_user.id)

    return incomes


@router.delete("/{income_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_income(
    session: SessionDep,
    income_id: int,
    current_user: CurrentUserDep,
) -> None:
    """Delete an income"""
    income: Income = crud.get_income_by_id(session, income_id)
    if not income:
        raise HTTPException(status_code=404, detail="Income not found")

    if income.user_id != current_user.id:
        raise HTTPException(
            status_code=403, detail="Not authorized to delete this income"
        )

    crud.delete_income(session, income)
    return None
