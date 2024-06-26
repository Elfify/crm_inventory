from contextlib import contextmanager

from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy_utils import create_database, database_exists

from crm_inventory.config.config import DATABASE_URL
from crm_inventory.data.exceptions import DatabaseInitializationException, DatabaseEngineException


_engine: Engine = create_engine(url=DATABASE_URL, pool_pre_ping=True)
TransactionalSession = sessionmaker(_engine)

def initialize_db():
    try:
        print("Initializing database...")

        if database_exists(DATABASE_URL):
            print("Database exists!")
        else:
            create_database(DATABASE_URL)
            print("Database created!")
    except Exception:
        raise DatabaseInitializationException

@contextmanager
def get_session() -> Session:
    session = TransactionalSession()

    try:
        yield session
    except Exception as e:
        raise DatabaseEngineException(str(e))
    finally:
        session.close()
