from db.models import User
from schemas import UserBasse
from sqlalchemy.orm import Session
from db.hash import Hash

def create_user(request: UserBasse, db: Session):
    user = User(
        username=request.username,
        password=Hash.bcrypt(request.password),
        email=request.email,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
