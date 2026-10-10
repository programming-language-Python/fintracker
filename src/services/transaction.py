from repositories import TransactionRepository
from schemas import TransactionCreateSchema, TransactionFilterSchema


class TransactionService:
    def __init__(self, repo: TransactionRepository):
        self.repo: TransactionRepository = repo()

    async def create(self, transaction: TransactionCreateSchema) -> int:
        transaction_dict = transaction.model_dump()
        transaction_id = await self.repo.create(transaction_dict)
        return transaction_id

    async def get(self, transaction_filter: TransactionFilterSchema):
        transactions = await self.repo.get(transaction_filter)
        return transactions

    async def update(self, transaction_id: int):
        pass
