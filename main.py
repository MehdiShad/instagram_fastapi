from fastapi import FastAPI
from db.models import Base
from db.database import engine
from routers import user

app = FastAPI()
app.include_router(user.router)


Base.metadata.create_all(engine)


@app.get('/', tags=['home_page'])
def home():
    return "home_page"