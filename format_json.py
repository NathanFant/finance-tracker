import json
import os

BUDGET = "budget.json"


def default_budget_structure() -> dict:
    """Returns the default budget structure."""
    return {
        "income": {
            "hourly": [],
            "weekly": [],
            "biweekly": [],
            "monthly": [],
            "yearly": [],
        },
        "expenses": {
            "weekly": [],
            "biweekly": [],
            "monthly": [],
            "yearly": [],
        },
    }


def prepare_json():
    """Prepares the JSON file for the project. Will start with empty dictionaries for expenses and income. Will futher break them down into categories."""
    if not os.path.exists(BUDGET):
        with open(BUDGET, "w") as file:
            data = default_budget_structure()
            json.dump(data, file, indent=4)
    else:
        with open(BUDGET, "r") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                print("JSON file is corrupted or empty. Creating a new one.")
                data = default_budget_structure()
        if "income" not in data:
            print("Income section not found in JSON. Adding default structure.")
            data["income"] = {
                "hourly": [],
                "weekly": [],
                "biweekly": [],
                "monthly": [],
                "yearly": [],
            }
        if "expenses" not in data:
            print("Expenses section not found in JSON. Adding default structure.")
            data["expenses"] = {
                "weekly": [],
                "biweekly": [],
                "monthly": [],
                "yearly": [],
            }
        with open(BUDGET, "w") as file:
            json.dump(data, file, indent=4)
    print("JSON file prepared or updated successfully.")


if __name__ == "__main__":
    prepare_json()
