from typing import Generic, Optional, TypeVar

from pydantic import BaseModel

from crm_inventory.data.inventory import Inventory
from crm_inventory.data.item import Item


ModelType = TypeVar('ModelType', bound=BaseModel)


class BaseResponse(BaseModel, Generic[ModelType]):
    result: str = "success"
    error: Optional[str] = None
    data: Optional[ModelType] = None


class InventoryResponse(BaseResponse[Inventory]):
    pass


# class ItemResponse(BaseResponse[Item]):
#     pass