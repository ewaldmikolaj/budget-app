from sqlmodel import Session, select

from core.models import (
    Expense,
    ExpenseCreate,
    ExpenseUpdate,
    ExpenseGet,
    Category,
)


def create_expense(session: Session, expense: ExpenseCreate, user_id: int) -> Expense:
    """Create a new expense"""
    object = Expense.model_validate(expense, update={"user_id": user_id})
    session.add(object)
    session.commit()
    session.refresh(object)
    return object


def get_expenses(session: Session, user_id: int) -> list[ExpenseGet]:
    """Get all expenses for a user"""
    statement = (
        select(Expense, Category)
        .join(Category, Expense.category_id == Category.id, isouter=True)
        .where(Expense.user_id == user_id)
    )
    result = session.exec(statement).all()
    expenses = []

    for expense, category in result:
        obj = ExpenseGet(
            id=expense.id,
            summary=expense.summary,
            amount=expense.amount,
            transaction_date=expense.transaction_date,
            category=category.name if category else None,
        )
        expenses.append(obj)
    return expenses


def get_expense_by_id(session: Session, expense_id: int) -> Expense | None:
    """Get an expense by ID"""
    statement = select(Expense).where(Expense.id == expense_id)
    result = session.exec(statement).first()
    return result


def delete_expense(session: Session, expense: Expense) -> None:
    """Delete an expense"""
    session.delete(expense)
    session.commit()
