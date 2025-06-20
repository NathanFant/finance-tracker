import json
from datetime import date
from pathlib import Path

from income_expenses.income_models import (
    HourlyIncome,
    WeeklyIncome,
    BiweeklyIncome,
    MonthlyIncome,
    YearlyIncome,
)

INCOME_CLASSES = {
    "hourly": HourlyIncome,
    "weekly": WeeklyIncome,
    "biweekly": BiweeklyIncome,
    "monthly": MonthlyIncome,
    "yearly": YearlyIncome,
}


def prompt_user(prompt, cast=str, optional=False):
    while True:
        val = input(f"{prompt}{' (optional)' if optional else ''}: ").strip()
        if optional and val == "":
            return None
        try:
            return cast(val)
        except ValueError:
            print(f"Invalid input. Please enter a valid {cast.__name__}.")


def add_income():
    """Function to add income to the budget JSON file."""

    budget_path = Path("budget.json")

    # load or create budget data
    if budget_path.exists():
        with open(budget_path, "r") as file:
            budget_data = json.load(file)
    else:
        budget_data = {"income": {}, "expenses": {}}

    income_type = ""
    while income_type not in INCOME_CLASSES:
        income_type = (
            input("Enter income type (hourly, weekly, biweekly, monthly, yearly): ")
            .strip()
            .lower()
        )
