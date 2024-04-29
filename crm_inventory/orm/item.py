from sqlalchemy import ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from crm_inventory.orm.base import Base
from crm_inventory.orm.mixins import TimestampMixin


class Item(Base, TimestampMixin):
    __tablename__ = "items"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    # inventory_id: Mapped[int] = mapped_column(Integer, ForeignKey('inventories.id'))
    SKU: Mapped[str]
    name: Mapped[str] = mapped_column(String(length=75))
    category: Mapped[str] = mapped_column(String, nullable=True)
    cost: Mapped[float]
    single_price: Mapped[float]
    total_quantity: Mapped[int] = mapped_column(Integer)
    current_quantity: Mapped[int] = mapped_column(Integer)
    stock_item: Mapped[bool]
    image_url: Mapped[str] = mapped_column(String, nullable=True)

    # inventory: Mapped["Inventory"] = relationship("Inventory", back_populates="items")
    # __table_args__ = (UniqueConstraint('SKU', 'inventory_id', name='_inventory_sku_uc'),)
