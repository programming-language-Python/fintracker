from api.transactions import router as router_transactions
from api.budgets import router as router_budgets
from api.reports import router as router_reports

all_routers = [
    router_transactions,
    router_budgets,
    router_reports
]
