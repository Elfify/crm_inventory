from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists

from crm_inventory.config.config import DATABASE_URL
from crm_inventory.data.exceptions import DatabaseInitializationException


def initialize_db():
    try:
        print("Initializing database...")

        if database_exists(DATABASE_URL):
            print("Database exists!")
        else:
            create_database(DATABASE_URL)
            print("Database created!")
    except Exception as e:
        raise DatabaseInitializationException
