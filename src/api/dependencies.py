from repositories import TransactionRepository, CategoryRepository
from services import TransactionService, CategoryService


def transaction_service() -> TransactionService:
    return TransactionService(TransactionRepository)


def category_service() -> CategoryService:
    return CategoryService(CategoryRepository)
