from repositories import TransactionRepository, CategoryRepository, BudgetRepository
from services import TransactionService, CategoryService, BudgetService


def transaction_service() -> TransactionService:
    return TransactionService(TransactionRepository)


def category_service() -> CategoryService:
    return CategoryService(CategoryRepository)

def budget_service() -> BudgetService:
    return BudgetService(BudgetRepository)