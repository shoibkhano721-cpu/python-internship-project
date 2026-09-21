import csv
import os

FILE_NAME = "expenses.csv"


def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ")
    description = input("Enter description: ")

    try:
        amount = float(input("Enter amount: "))

        file_exists = os.path.exists(FILE_NAME)

        with open(FILE_NAME, "a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(["Date", "Category", "Description", "Amount"])

            writer.writerow([date, category, description, amount])

        print("Expense added successfully!")

    except ValueError:
        print("Please enter a valid amount.")


def view_expenses():
    if not os.path.exists(FILE_NAME):
        print("No expenses found.")
        return

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        print("\n--- All Expenses ---")

        for row in reader:
            print(
                row["Date"], "|",
                row["Category"], "|",
                row["Description"], "| ₹",
                row["Amount"]
            )


def filter_expenses():
    if not os.path.exists(FILE_NAME):
        print("No expenses found.")
        return

    category = input("Enter category to filter: ").lower()

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        found = False

        print("\n--- Filtered Expenses ---")

        for row in reader:
            if row["Category"].lower() == category:
                print(
                    row["Date"], "|",
                    row["Description"], "| ₹",
                    row["Amount"]
                )
                found = True

        if not found:
            print("No expenses found in this category.")


def category_summary():
    if not os.path.exists(FILE_NAME):
        print("No expenses found.")
        return

    summary = {}

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            category = row["Category"]
            amount = float(row["Amount"])

            if category in summary:
                summary[category] += amount
            else:
                summary[category] = amount

    print("\n--- Category Summary ---")

    for category, total in summary.items():
        print(category, ": ₹", total)


while True:
    print("\n===== Personal Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Filter Expenses")
    print("4. Category Summary")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        filter_expenses()

    elif choice == "4":
        category_summary()

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")