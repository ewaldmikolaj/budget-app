from sqlmodel import Session, select

from core.models import Income, IncomeCreate, IncomeGet


def create_income(session: Session, income: IncomeCreate, user_id: int) -> Income:
    """Create a new income"""
    object = Income.model_validate(income, update={"user_id": user_id})
    session.add(object)
    session.commit()
    session.refresh(object)
    return object


def get_incomes(session: Session, user_id: int) -> list[IncomeGet]:
    """Get all incomes for a user"""
    statement = select(Income).where(Income.user_id == user_id)
    result = session.exec(statement).all()
    incomes = [IncomeGet(**income.model_dump(exclude={user_id})) for income in result]
    return incomes


def get_income_by_id(session: Session, income_id: int) -> Income | None:
    """Get an income by ID"""
    statement = select(Income).where(Income.id == income_id)
    result = session.exec(statement).first()
    return result


def delete_income(session: Session, income: Income) -> None:
    """Delete an income"""
    session.delete(income)
    session.commit()
