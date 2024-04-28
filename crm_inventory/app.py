from contextlib import asynccontextmanager

from fastapi import FastAPI

from crm_inventory.utils.db import initialize_db, initialize_engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    initialize_db()
    initialize_engine()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/health")
def health():
    return {
        'result': 'GOOD'
    }
