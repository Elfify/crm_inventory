from contextlib import asynccontextmanager

from fastapi import FastAPI

from crm_inventory.config.config import initialize_db

app = FastAPI()


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("creating DB")
    initialize_db()
    yield


@app.get("/health")
def health():
    return {
        'result': 'GOOD'
    }
