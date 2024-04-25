from sqlalchemy_utils import create_database, database_exists
from crm_inventory.config.config import DATABASE_URL

def test__db_exists():
    assert database_exists(DATABASE_URL) is True