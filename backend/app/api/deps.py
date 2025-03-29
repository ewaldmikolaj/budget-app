from collections.abc import Generator
from typing import Annotated

from fastapi import Depends
from sqlmodel import Session

from core.db import engine

def get_db() -> Generator[Session, None, None]:
    """
    Dependency that provides a database session for the duration of a request.
    """
    with Session(engine) as session:
        yield session
    
SessionDep = Annotated[Session, Depends(get_db)]