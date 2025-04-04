from sqlmodel import Session, select

from core.models import Expense, ExpenseCreate, ExpenseUpdate


def create_expense(session: Session, expense: ExpenseCreate, user_id: int) -> Expense:
    """Create a new expense"""
    object = Expense.model_validate(expense, update={"user_id": user_id})
    session.add(object)
    session.commit()
    session.refresh(object)
    return object
