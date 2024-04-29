import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine

from crm_inventory.app import app
from crm_inventory.utils.db import get_session, TransactionalSession
from tests.utils.db import clean_database


@pytest.fixture
def db_engine():
    engine = create_engine("postgresql://postgres:postgres@localhost:5432/crm_inventory-test")

    return engine

@pytest.fixture
def test_client() -> TestClient:
    return TestClient(app)

@pytest.fixture
def initialize_and_clean_db():
    session = TransactionalSession()
    yield session
    clean_database(session)
