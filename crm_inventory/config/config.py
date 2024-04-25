from sqlalchemy_utils import create_database, database_exists

DATABASE_URL = "postgresql://postgres:postgres@postgres-local:5432/crm_inventory"

def initialize_db():
    print("Creating database...")

    if database_exists(DATABASE_URL):
        print("Database exists!")
    else:
        create_database(DATABASE_URL)
        print("Database created!")