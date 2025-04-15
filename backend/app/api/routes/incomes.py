from fastapi import APIRouter

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
