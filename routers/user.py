from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas import UserDisplay, UserBasse

from db.database import get_db
from db import db_user
router = APIRouter(prefix='/user', tags=['user'])


@router.post('', response_model=UserDisplay)
def create_user(request: UserBasse, db: Session=Depends(get_db)):
    return db_user.create_user(request=request, db=db)


