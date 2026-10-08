from schemas import TransactionCreateSchema
from utils.repository import AbstractRepository


class TransactionService:
    def __init__(self, repo: AbstractRepository):
        self.repo: AbstractRepository = repo()

    async def create(self, transaction: TransactionCreateSchema) -> int:
        transaction_dict = transaction.model_dump()
        transaction_id = await self.repo.create(transaction_dict)
        return transaction_id

    async def get(self):
        pass

    async def update(self, transaction_id: int):
        pass
