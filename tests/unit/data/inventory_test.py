import pytest

from pydantic import ValidationError

from crm_inventory.data.inventory import Inventory


def test__inventory__required_vars():
    # Arrange
    json = {"user_id": 1, "name": "TEST_NAME", "storage_location": "TEST_STORAGE_LOCATION"}
    
    # Act
    inventory = Inventory(**json)
    
    # Assert
    expected_json = {"id": None, "user_id": 1, "name": "TEST_NAME", "storage_location": "TEST_STORAGE_LOCATION"}
    assert inventory.model_dump() == expected_json


def test__inventory__missing_required_vars():
    # Arrange
    json = {"name": "TEST_NAME", "storage_location": "TEST_STORAGE_LOCATION"}
    
    # Act / Assert
    with pytest.raises(ValidationError):
        Inventory(**json)
