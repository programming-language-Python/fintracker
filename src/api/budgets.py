from fastapi import APIRouter

router = APIRouter(
    prefix="/budgets",
    tags=["Budgets"],
)


@router.post("")
async def create_budgets():
    pass


@router.get("")
async def get_budgets():
    pass
