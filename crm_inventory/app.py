import os
from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, Response, status

from crm_inventory.data.requests import CreateInventoryRequest
from crm_inventory.data.responses import InventoryResponse
from crm_inventory.repositories.inventory_repository import InventoryRepository
from crm_inventory.services.inventory_service import InventoryService
from crm_inventory.utils.db import  get_session, initialize_db, TransactionalSession


@asynccontextmanager
async def lifespan(app: FastAPI):
    initialize_db()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/health")
def health():
    return {
        'result': 'GOOD'
    }


@app.post(
        "/inventory",
        response_model=InventoryResponse,
        response_model_exclude_none=True,
        status_code=status.HTTP_201_CREATED
) 
def create_inventory(
    request_params: CreateInventoryRequest,
    response: Response,
    session: TransactionalSession = Depends(get_session)
):
    inventory_repository = InventoryRepository(session=session)
    inventory_service = InventoryService(inventory_repository=inventory_repository)

    try:
        inventory = inventory_service.create_inventory(record=request_params)
        return InventoryResponse(data=inventory)
    except Exception as e:
        response.status_code = 500
        return InventoryResponse(result="failure", error=str(e))
