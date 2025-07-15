from app.main import app
from app.database import get_db, Base
from app.entities import tasks

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL="sqlite:///./test_tsk.db"

engine = create_engine(DATABASE_URL, connect_args={
    "check_same_thread": False,
    })

TestSessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

def overide_get_db():
    session = TestSessionLocal()
    try:
        yield session
    finally:
        session.close()
        
app.dependency_overrides[get_db] = overide_get_db


@pytest.fixture(scope="session", autouse=True)
def setup_db():
    # create tables before session and TestClient starts
    Base.metadata.create_all(bind=engine)
    yield
    # drop tables after all test runs
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def session():
    db = TestSessionLocal()
    yield db
    db.close()


@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c


@pytest.fixture
def dummy_data(session):
    dummy = tasks.Tasks(title="New Task", description="Used to test")
    
    session.add(dummy)
    session.commit()
    
    yield dummy
