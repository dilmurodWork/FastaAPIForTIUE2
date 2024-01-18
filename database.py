from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = 'sqlite:///music_app.db'

engine = create_engine(DATABASE_URL,
                       connect_args={'check_same_thread': False})

SessionLocale = sessionmaker(bind=engine)
Base = declarative_base()
