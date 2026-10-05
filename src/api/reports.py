from fastapi import APIRouter

router = APIRouter(
    prefix="/reports",
    tags=["Reports"],
)


@router.get("/categories")
async def get_categories():
    pass


@router.get("/timeseries")
async def get_timeseries():
    pass
