from typing import Annotated

from fastapi import APIRouter, Depends

from schemas import TransactionCreateSchema, TransactionSchema, TransactionFilterSchema, TransactionUpdateSchema
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
async def get_transactions(
        transaction_filter: Annotated[TransactionFilterSchema, Depends()],
        transaction_service: Annotated[TransactionService, Depends(transaction_service)],
) -> list[TransactionSchema]:
    transactions = await transaction_service.get(transaction_filter)
    return transactions


@router.patch("/{transaction_id}")
async def update_transactions(
        transaction_id: int,
        transaction: Annotated[TransactionUpdateSchema, Depends()],
        transaction_service: Annotated[TransactionService, Depends(transaction_service)],
) -> TransactionSchema:
    transaction = await transaction_service.update(transaction_id, transaction)
    return transaction
