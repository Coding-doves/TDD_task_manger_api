import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

load_dotenv()


DATABASE_URL=os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

Session = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()


def get_db():
    session = Session()
    try:
        yield session
    finally:
        session.close()
