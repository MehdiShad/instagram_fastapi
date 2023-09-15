import shutil
import random
from fastapi import APIRouter, Depends, status, UploadFile, File
from fastapi.exceptions import HTTPException
from db import db_post
from schemas import PostBase, PostDisplay,UserAuth
from sqlalchemy.orm import Session
from db.database import get_db
from typing import List
from string import ascii_letters
from auth import oauth2


router = APIRouter(prefix='/post', tags=['post'])

image_url_types = ["url", "uploaded"]


@router.post(path='/create_post', response_model=PostDisplay)
def create_post(request: PostBase, db: Session = Depends(get_db), current_user: UserAuth=Depends(oauth2.get_current_user)):
    if request.image_url_type not in image_url_types:
        return HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                             detail="image url type should be url or uploaded")
    return db_post.create_post(request=request, db=db)


@router.get("/", response_model=List[PostDisplay])
def get_posts(db: Session=Depends(get_db)):
    return db_post.get_all_post(db=db)

@router.post("/upload_file")
def upload_file(file: UploadFile=File(...)):
    rand_str = ''.join(random.choice(ascii_letters) for _ in range(6))
    new_name = f"_{rand_str}.".join(file.filename.rsplit('.', 1))

    path_file = f"uploaded_files/{new_name}"
    with open(path_file, 'w+b') as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"path_file": path_file}