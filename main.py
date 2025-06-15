from datetime import date, datetime
import income_expenses
from navigate import navigate

"""For now, this will be a CLI budget app. Will only track expenses and income.
In the future, it will be a full-fledged budget app with a GUI and more features.
"""


def main():
    print("Welcome to the Budget App!")
    print("This is a CLI budget app for tracking expenses and income.")
    print(
        "In the future, it will be a full-fledged budget app with a GUI and more features."
    )
    print(
        "Current date:",
        datetime.now().strftime("%Y-%m-%d"),
        "Time:",
        datetime.now().strftime("%I:%M %p"),  # 12 hr format
    )
    navigate()
    # Here you can add more functionality like adding expenses, income, etc.
    # For now, we will just exit the app.
    print("Exiting the app. Goodbye!")
    exit(0)


if __name__ == "__main__":
    main()
