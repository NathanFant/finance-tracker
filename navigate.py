def navigate():
    """Navigate through the budget app."""
    print("Welcome to the Budget App!")
    print("1. View Budget")
    print("2. Go To Income")
    print("3. Go To Expenses")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Viewing budget...")
        # Logic to view budget
    elif choice == "2":
        print("Going to income...")
        # Logic to add income
    elif choice == "3":
        print("Going to expenses...")
        # Logic to add expense
    elif choice == "0":
        pass  # Exit the app
    else:
        print("Invalid choice, please try again.")
