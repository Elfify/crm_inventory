from sqlalchemy import MetaData


def test__items_table_exists(db_engine):
    metadata = MetaData()
    metadata.reflect(bind=db_engine)
    
    assert "items" in metadata.tables.keys()
