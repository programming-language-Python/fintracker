from fastapi import APIRouter

router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"],
)


@router.post("")
async def create_transactions():
    pass


@router.get("")
async def get_transactions():
    pass


@router.put("")
async def update_transactions(transaction_id: int):
    pass
