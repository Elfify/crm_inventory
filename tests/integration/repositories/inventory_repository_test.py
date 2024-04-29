from crm_inventory.data.inventory import Inventory
from crm_inventory.repositories.inventory_repository import InventoryRepository


def test__create_inventory__success(initialize_and_clean_db):
    # Arrange
    session = initialize_and_clean_db
    inventory = Inventory(**{"user_id": 1, "name": "TEST_NAME", "storage_location": "TEST_STORAGE_LOCATION"})
    inventory_repository = InventoryRepository(session=session)
    
    # Act
    new_inventory = inventory_repository.create_record(inventory)

    # Assert
    expected_inventory = Inventory(id=1, user_id=1, name='TEST_NAME', storage_location='TEST_STORAGE_LOCATION')
    assert new_inventory == expected_inventory
