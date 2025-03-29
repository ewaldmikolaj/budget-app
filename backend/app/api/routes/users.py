from fastapi import APIRouter, HTTPException

from core.models import User, UserCreate, UserUpdate
from core import crud
from ..deps import SessionDep

router = APIRouter(prefix="/users", tags=["auth"])


@router.post("/", response_model=User)
def create_user(session: SessionDep, user: UserCreate) -> User:
    """Creates a new user"""
    user = crud.create_user(session, user)
    if not user:
        raise HTTPException(status_code=400, detail="User already exists")
    return user
