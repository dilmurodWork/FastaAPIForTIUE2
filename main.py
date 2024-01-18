from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models
from database import engine, SessionLocale
from typing import Annotated
from pydantic import BaseModel

app = FastAPI(
    title='Music APP',
    version='0.0.1'
)


def get_db():
    db = SessionLocale()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


class MusicForm(BaseModel):
    title: str
    author: int


@app.get('/')
async def hello(db: db_dependency):
    return db.query(models.Music).all()


class AuthorForm(BaseModel):
    full_name: str


@app.post('/create/author', status_code=201)
async def create_music(db: db_dependency, author_form_request: AuthorForm = Depends()):
    author_model = models.Author(**author_form_request.__dict__)

    db.add(author_model)
    db.commit()


@app.post('/create', status_code=201)
async def create_music(db: db_dependency, music_form_request: MusicForm = Depends()):
    music_model = models.Music(**music_form_request.__dict__)

    db.add(music_model)
    db.commit()


models.Base.metadata.create_all(bind=engine)
