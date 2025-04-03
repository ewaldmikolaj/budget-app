from fastapi import APIRouter, HTTPException

from core.models import User, UserCreate, UserMe
from core import crud
from ..deps import SessionDep, CurrentUserDep

router = APIRouter(prefix="/users")


@router.post("", response_model=User)
def create_user(session: SessionDep, user: UserCreate) -> User:
    """Creates a new user"""
    user = crud.create_user(session, user)
    if not user:
        raise HTTPException(status_code=400, detail="User already exists")

    return user


@router.get("/me", response_model=UserMe)
def read_user_me(current_user: CurrentUserDep) -> UserMe:
    """Get the current user"""
    return UserMe(
        id=current_user.id,
        email=current_user.email,
        name=current_user.name,
        surname=current_user.surname,
    )
