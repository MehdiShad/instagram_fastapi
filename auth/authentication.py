from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from db.database import get_db
from db import models
from db.hash import Hash
from auth import oauth2

router = APIRouter(prefix='', tags=['authentication'])


def get_token(request: OAuth2PasswordRequestForm=Depends(), db: Session=Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == request.username).first()
    if not user:
        print("sdf")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credential")

    if not Hash.verify(user.password, request.password):
        print("sdfsd")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid password")

    access_token = oauth2.create_access_token(data={'sub': request.username})

    return {
        'access_token': access_token,
        'type_token': "Bearer",
        'userID': user.id,
        'username': user.username,
    }


