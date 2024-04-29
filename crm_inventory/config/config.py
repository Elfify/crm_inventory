import os


env = os.getenv('APP_ENV', 'test')

DATABASE_URL = f"postgresql://postgres:postgres@postgres-local:5432/crm_inventory-{env}"
