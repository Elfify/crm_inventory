from sqlalchemy.orm import Session

from crm_inventory.data.inventory import Inventory
from crm_inventory.data.requests import CreateInventoryRequest
from crm_inventory.orm.inventory import Inventory as InventoryORM
from crm_inventory.repositories.base import AbstractRepository


class InventoryRepository(AbstractRepository):
    def __init__(self, session: Session):
        self.session = session

    def create_record(self, record: Inventory) -> Inventory:
        with self.session as session:
            inventory = InventoryORM(**record.model_dump())
            session.add(inventory)
            session.commit()
            new_inventory = Inventory.model_validate(inventory)

        return new_inventory
