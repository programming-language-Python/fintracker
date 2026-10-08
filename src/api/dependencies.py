from repositories import TransactionRepository
from services.transaction import TransactionService


def transaction_service() -> TransactionService:
    return TransactionService(TransactionRepository())
