from sqlmodel import Session

from ..models import User
from .user import get_user_by_email
from ..security import verify_password


def authenticate(session: Session, email: str, password: str) -> User | None:
    """Authenticate a user by email and password"""
    user = get_user_by_email(session, email)
    if not user:
        return None
    if not verify_password(password, user.password):
        return None
    return user
