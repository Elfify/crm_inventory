from sqlalchemy import create_engine, MetaData
from crm_inventory.config.config import DATABASE_URL


def test__items_table_exists():
    engine = create_engine("postgresql://postgres:postgres@localhost:5432/crm_inventory")
    metadata = MetaData()
    metadata.reflect(bind=engine)
    
    assert "items" in metadata.tables.keys()
