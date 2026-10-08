from typing import Annotated

from fastapi import APIRouter, Depends

from schemas import TransactionCreateSchema
from services.transaction import TransactionService
from .dependencies import transaction_service

router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"],
)


@router.post("")
async def create_transactions(
        transaction: Annotated[TransactionCreateSchema, Depends()],
        transaction_service: Annotated[TransactionService, Depends(transaction_service)],
):
    transaction_id = await transaction_service.create(transaction)
    return {"transaction_id": transaction_id}


@router.get("")
async def get_transactions():
    pass


@router.put("")
async def update_transactions(transaction_id: int):
    pass
