from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from crm_inventory.orm.base import Base
from crm_inventory.orm.mixins import TimestampMixin


class Inventory(Base, TimestampMixin):
    __tablename__ = "inventories"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int]
    name: Mapped[str] = mapped_column(String(length=75))
    storage_location: Mapped[str]
    # items: Mapped[list] = relationship("Item", back_populates="inventory")
