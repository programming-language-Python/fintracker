from schemas import CategoryCreateSchema
from utils.repository import AbstractRepository


class CategoryService:
    def __init__(self, repo: AbstractRepository):
        self.repo: AbstractRepository = repo()

    async def create(self, category: CategoryCreateSchema) -> int:
        category_dict = category.model_dump()
        category_id = await self.repo.create(category_dict)
        return category_id

    async def get(self):
        pass
