from datetime import datetime


def generate_expense_id(expenses):
   if not expenses:
       return "E1001"
   last_id = max(int(e["id"][1:]) for e in expenses)
   return f"E{last_id + 1}"

def get_valid_amount(prompt):
    
    try:
        amount = float(input(prompt))
        if amount <= 0:
            return None
        return amount
    except ValueError:
        return None


def get_valid_date(prompt):
   
    date_input = input(prompt).strip()
    try:
        datetime.strptime(date_input, "%Y-%m-%d")
        return date_input
    except ValueError:
        return None


def calculate_total_expense(expenses):
    
    return sum(expense["amount"] for expense in expenses)


def calculate_category_totals(expenses):
   
    category_totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category not in category_totals:
            category_totals[category] = 0

        category_totals[category] += amount

    return category_totals


def find_highest_expense(expenses):
    
    if not expenses:
        return None

    highest = expenses[0]

    for expense in expenses:
        if expense["amount"] > highest["amount"]:
            highest = expense

    return highest
