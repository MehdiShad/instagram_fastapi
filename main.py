from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from db.models import Base
from db.database import engine
from routers import user, post

app = FastAPI()
app.include_router(user.router)
app.include_router(post.router)

app.mount("/files", StaticFiles(directory="uploaded_files"), name="files")

Base.metadata.create_all(engine)


@app.get('/', tags=['home_page'])
def home():
    return "home_page"