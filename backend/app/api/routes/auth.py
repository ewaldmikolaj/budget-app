from fastapi import APIRouter, HTTPException, Response
from datetime import timedelta

from core import crud
from core import security
from ..deps import SessionDep, OAuthFormDep

router = APIRouter(prefix="/auth", tags=["auth"])

ACCESS_TOKEN_EXPIRE_MINUTES = 30


@router.post("/token")
def login_for_access_token(session: SessionDep, data: OAuthFormDep, response: Response):
    """Login and get access token"""
    user = crud.authenticate(session, data.username, data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = security.create_access_token(user.email, access_token_expires)
    response.set_cookie(key="access_token", value=access_token, httponly=True)

    return {"message": "success"}
