from utils import (
    generate_expense_id,
    get_valid_amount,
    get_valid_date,
    calculate_category_totals,
    calculate_total_expense,
    find_highest_expense
)

expenses = []


def add_expense():
    amount = get_valid_amount("Enter amount (positive number only): ")
    if amount is None:
        print("❌ Invalid amount")
        return

    category = input("Enter category: ").strip().lower()
    if not category:
        print("❌ Category cannot be empty")
        return

    note = input("Enter note (optional): ").strip()

    date = get_valid_date("Enter date (YYYY-MM-DD): ")
    if date is None:
        print("❌ Invalid format! Please use YYYY-MM-DD (e.g., 2026-01-09).")
        return

    expense = {
        "id": generate_expense_id(expenses),
        "amount": amount,
        "category": category,
        "note": note,
        "date": date
    }

    expenses.append(expense)
    print(f"✅ Expense {expense['id']} added successfully")


def view_expenses():
    if not expenses:
        print("⚠️ No expenses recorded yet")
        return

    for expense in expenses:
        print("-" * 30)
        print(f"ID       : {expense['id']}")
        print(f"Amount   : {expense['amount']}")
        print(f"Category : {expense['category']}")
        print(f"Note     : {expense['note']}")
        print(f"Date     : {expense['date']}")
    print("-" * 30)


def show_summary():
    if not expenses:
        print("⚠️ No expenses to summarize")
        return

    total = calculate_total_expense(expenses)
    category_totals = calculate_category_totals(expenses)
    highest = find_highest_expense(expenses)

    print("\n📊 Expense Summary")
    print(f"Total Expense: {total}")

    print("\nCategory-wise Totals:")
    for category, amount in category_totals.items():
        print(f"{category} → {amount}")

    print("\nHighest Expense:")
    if highest:
        print(f"ID       : {highest['id']}")
        print(f"Amount   : {highest['amount']}")
        print(f"Category : {highest['category']}")
        print(f"Note     : {highest['note']}")
        print(f"Date     : {highest['date']}")
    else:
        print("No expenses recorded.")

def show_menu():
    print("\n💰 Expense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Expense Summary")
    print("4. Exit")


while True:
    show_menu()

    try:
        choice = int(input("Enter choice (1-4): "))

        if choice == 1:
            add_expense()
        elif choice == 2:
            view_expenses()
        elif choice == 3:
            show_summary()
        elif choice == 4:
            print("👋 Exiting Expense Tracker")
            break
        else:
            print("❌ Invalid choice")

    except ValueError:
        print("❌ Enter numeric value only")
