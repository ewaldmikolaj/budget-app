from fastapi import APIRouter

from core.models import User

router = APIRouter(prefix="/user", tags=["auth"])