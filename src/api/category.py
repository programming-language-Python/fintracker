from typing import Annotated

from fastapi import APIRouter, Depends

from schemas import CategoryCreateSchema
from services.category import CategoryService
from .dependencies import category_service

router = APIRouter(
    prefix="/categories",
    tags=["Categories"],
)


@router.post("")
async def create_categories(
        category: Annotated[CategoryCreateSchema, Depends()],
        category_service: Annotated[CategoryService, Depends(category_service)],
):
    category_id = await category_service.create(category)
    return {"category_id": category_id}
