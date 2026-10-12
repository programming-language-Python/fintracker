import asyncio
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from faker import Faker
from sqlalchemy import delete, select

from db.db import async_session_maker
from enums import TransactionType
from models import Budget, Category, Transaction

fake = Faker("ru_RU")

CATEGORIES_COUNT = 10
TRANSACTIONS_COUNT = 200
BUDGETS_COUNT = 20
PERIOD_DAYS = 365


def build_category_names() -> set[str]:
    return {fake.unique.word().capitalize() for _ in range(CATEGORIES_COUNT)}


def build_transactions(category_ids: list[int]) -> list[Transaction]:
    now = datetime.now()
    return [
        Transaction(
            type=fake.random_element(list(TransactionType)),
            sum=fake.pyfloat(min_value=10, max_value=100_000, right_digits=2),
            description=fake.sentence(nb_words=4),
            occurred_on=now - timedelta(days=fake.random_int(0, PERIOD_DAYS)),
            category_id=fake.random_element(category_ids),
        )
        for _ in range(TRANSACTIONS_COUNT)
    ]


def build_budgets(category_ids: list[int]) -> list[Budget]:
    today = date.today()
    return [
        Budget(
            limit_amount=fake.pyfloat(min_value=1_000, max_value=500_000, right_digits=2),
            period_month=(today - timedelta(days=fake.random_int(0, PERIOD_DAYS))).replace(day=1),
            category_id=fake.random_element(category_ids),
        )
        for _ in range(BUDGETS_COUNT)
    ]


async def fill_db() -> None:
    async with async_session_maker() as session:
        await session.execute(delete(Transaction))
        await session.execute(delete(Budget))
        await session.execute(delete(Category))

        categories = [Category(name=name) for name in build_category_names()]
        session.add_all(categories)
        await session.flush()

        category_ids = (await session.scalars(select(Category.id))).all()

        session.add_all(build_transactions(category_ids))
        session.add_all(build_budgets(category_ids))
        await session.commit()

    print(
        f"Seeded: {len(categories)} categories, "
        f"{TRANSACTIONS_COUNT} transactions, {BUDGETS_COUNT} budgets"
    )


if __name__ == "__main__":
    asyncio.run(fill_db())
