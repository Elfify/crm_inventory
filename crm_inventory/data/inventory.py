from typing import Optional

from pydantic import BaseModel, Field


class Inventory(BaseModel):
    id: Optional[int] = None
    user_id: int
    name: str
    storage_location: str = Field(max_length=75)

    class Config:
        from_attributes = True
