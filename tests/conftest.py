import pytest
from fastapi.testclient import TestClient

from crm_inventory.app import app


@pytest.fixture
def test_client() -> TestClient:
    return TestClient(app)
