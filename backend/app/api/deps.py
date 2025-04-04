import jwt
import base64

from collections.abc import Generator
from typing import Annotated

from fastapi import HTTPException, Request, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlmodel import Session

from core.db import engine
from core.security import SECRET_KEY, ALGORITHM
from core import crud
from core.models import User

reusable_oauth2 = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/token")


def get_db() -> Generator[Session, None, None]:
    """Dependency that provides a database session for the duration of a request."""
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_db)]
TokenDep = Annotated[str, Depends(reusable_oauth2)]
OAuthFormDep = Annotated[OAuth2PasswordRequestForm, Depends()]


async def get_current_user(session: SessionDep, request: Request) -> User:
    """Dependency that retrieves the current user from the token."""
    exception = HTTPException(status_code=401, detail="Not authenticated")
    try:
        token = request.cookies.get("access_token")
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        if email is None:
            raise exception
    except jwt.exceptions.InvalidTokenError as err:
        raise exception
    user = crud.get_user_by_email(session, email)
    if user is None:
        raise exception
    return user


CurrentUserDep = Annotated[User, Depends(get_current_user)]
