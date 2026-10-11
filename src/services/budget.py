from schemas import BudgetCreateSchema
from utils.repository import AbstractRepository


class BudgetService:

    def __init__(self, repo: AbstractRepository):
        self.repo: AbstractRepository = repo()

    async def create(self, budget: BudgetCreateSchema):
        budget_dict = budget.model_dump()
        budget_id = await self.repo.create(budget_dict)
        return budget_id

    async def get(self):
        budgets = await self.repo.get()
        return budgets
