from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base


class User(Base):
    __tablename__ = "user"

    id = Column('id', Integer, index=True, primary_key=True)
    username = Column('username', String)
    password = Column('password', String)
    email = Column('email', String)
    items = relationship("Post", back_populates='user')


class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, index=True, primary_key=True)
    image_url = Column(String)
    image_url_type = Column(String)
    caption = Column(String)
    timestamp = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", back_populates="items")