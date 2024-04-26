import pytest
from sqlalchemy import create_engine

@pytest.fixture
def db_engine():
    engine = create_engine("postgresql://postgres:postgres@localhost:5432/crm_inventory")

    return engine
