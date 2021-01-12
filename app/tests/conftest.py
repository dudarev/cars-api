import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ..database import Base
from ..main import app, get_db
from ..models import Make, Model, Submodel, Car

from .fixtures_data import MAKE_FIXTURE_DATA, MODEL_FIXTURE_DATA, SUBMODEL_FIXTURE_DATA, CAR_FIXTURE_DATA

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


@pytest.fixture
def client():
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)


@pytest.fixture
def db_fixture():
    db = TestingSessionLocal()
    for data in MAKE_FIXTURE_DATA:
        db.add(Make(**data))
    for data in MODEL_FIXTURE_DATA:
        db.add(Model(**data))
    for data in SUBMODEL_FIXTURE_DATA:
        db.add(Submodel(**data))
    for data in CAR_FIXTURE_DATA:
        db.add(Car(**data))
    db.commit()
    yield
    db.query(Car).delete()
    db.query(Submodel).delete()
    db.query(Model).delete()
    db.query(Make).delete()
    db.commit()
    db.close()
