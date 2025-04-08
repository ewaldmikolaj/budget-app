from sqlmodel import Session, select

from core.models import (
    Expense,
    ExpenseCreate,
    ExpenseUpdate,
    ExpenseWithCategory,
    Category,
)


def create_expense(session: Session, expense: ExpenseCreate, user_id: int) -> Expense:
    """Create a new expense"""
    object = Expense.model_validate(expense, update={"user_id": user_id})
    session.add(object)
    session.commit()
    session.refresh(object)
    return object


def get_expenses(session: Session, user_id: int) -> list[ExpenseWithCategory]:
    """Get all expenses for a user"""
    statement = (
        select(Expense, Category)
        .join(Category, Expense.category_id == Category.id, isouter=True)
        .where(Expense.user_id == user_id)
    )
    result = session.exec(statement).all()
    expenses = []

    for expense, category in result:
        obj = ExpenseWithCategory(
            id=expense.id,
            summary=expense.summary,
            amount=expense.amount,
            transaction_date=expense.transaction_date,
            category=category.name,
        )
        expenses.append(obj)
    return expenses
