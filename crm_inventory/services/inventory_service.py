from crm_inventory.data.inventory import Inventory
from crm_inventory.data.requests import CreateInventoryRequest
from crm_inventory.repositories.inventory_repository import InventoryRepository


class InventoryService:
    def __init__(
            self,
            inventory_repository: InventoryRepository
    ):
        self.inventory_repository = inventory_repository
    
    def create_inventory(self, record: CreateInventoryRequest):
        inventory = Inventory(**record.model_dump())

        try:
            new_inventory = self.inventory_repository.create_record(inventory)
        except Exception as e:
            print(str(e))
            raise e
        
        return new_inventory