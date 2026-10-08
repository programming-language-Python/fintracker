from models import Budget
from utils.repository import SQLAlchemyRepository


class BudgetRepository(SQLAlchemyRepository):
    model = Budget
