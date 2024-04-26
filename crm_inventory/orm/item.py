from sqlalchemy import Integer, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from crm_inventory.orm.base import Base
from crm_inventory.orm.mixins import TimestampMixin


class Item(Base, TimestampMixin):
    __tablename__ = "items"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    SKU: Mapped[str]
    name: Mapped[str] = mapped_column(String(length=75))
    category: Mapped[str]
    cost: Mapped[float]
    single_price: Mapped[float]
    total_quantity: Mapped[int] = mapped_column(Integer)
    current_quantity: Mapped[int] = mapped_column(Integer)
    stock_item: Mapped[bool]
    image_url: Mapped[str]

    inventory_id: Mapped[int] = relationship("Inventory", back_populates="items")
    __table_args__ = (UniqueConstraint('sku', 'inventory_id', name='_inventory_sku_uc'),)
