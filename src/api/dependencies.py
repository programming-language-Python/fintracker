from repositories import TransactionRepository, CategoryRepository, BudgetRepository, ReportRepository
from services import TransactionService, CategoryService, BudgetService, ReportService


def transaction_service() -> TransactionService:
    return TransactionService(TransactionRepository)


def category_service() -> CategoryService:
    return CategoryService(CategoryRepository)


def budget_service() -> BudgetService:
    return BudgetService(BudgetRepository)


def report_service() -> ReportService:
    return ReportService(ReportRepository)
