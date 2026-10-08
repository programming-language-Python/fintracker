from models import Transaction
from utils.repository import SQLAlchemyRepository


class TransactionRepository(SQLAlchemyRepository):
    model = Transaction

    async def update(self, transaction_id: int):
        pass
