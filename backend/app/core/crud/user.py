from sqlmodel import Session, select

from core.models import User, UserCreate
from core.security import pwd_context


def get_user_by_email(session: Session, email: str) -> User | None:
    """Get a user by email"""
    stmt = select(User).where(User.email == email)
    return session.exec(stmt).first()


def create_user(session: Session, user: UserCreate) -> User:
    """Create a new user"""
    object = User.model_validate(
        user, update={"password": pwd_context.hash(user.password)}
    )
    session.add(object)
    session.commit()
    session.refresh(object)
    return object
