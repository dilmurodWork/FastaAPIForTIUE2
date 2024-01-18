import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP
from database import Base


class Music(Base):
    __tablename__ = 'musics'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(Integer, ForeignKey('authors.id'))
    created_at = Column(TIMESTAMP, default=datetime.datetime.now)


class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String)
