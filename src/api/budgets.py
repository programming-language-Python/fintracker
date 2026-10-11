from typing import Annotated

from fastapi import APIRouter, Depends

from schemas import BudgetCreateSchema
from services import BudgetService
from .dependencies import budget_service

router = APIRouter(
    prefix="/budgets",
    tags=["Budgets"],
)


@router.post("")
async def create_budgets(
        budget: Annotated[BudgetCreateSchema, Depends()],
        budget_service: Annotated[BudgetService, Depends(budget_service)]
):
    budget_id = await budget_service.create(budget)
    return {"budget_id": budget_id}


@router.get("")
async def get_budgets():
    pass
