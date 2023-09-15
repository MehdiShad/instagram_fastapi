import datetime
from db.models import Post
from schemas import PostBase,PostDisplay
from sqlalchemy.orm import Session


def create_post(request: PostBase, db: Session):
    new_post = Post(
        image_url=request.image_url,
        image_url_type=request.image_url_type,
        caption=request.caption,
        timestamp=datetime.datetime.now(),
        user_id=request.creator_id,
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


def get_all_post(db: Session):
    return db.query(Post).all()
