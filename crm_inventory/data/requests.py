from pydantic import BaseModel


class CreateInventoryRequest(BaseModel):
    user_id: int
    name: str
    storage_location: str
