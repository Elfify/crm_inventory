from sqlalchemy import MetaData


def test__inventories_table_exists(db_engine):
    metadata = MetaData()
    metadata.reflect(bind=db_engine)

    assert "inventories" in metadata.tables.keys()
