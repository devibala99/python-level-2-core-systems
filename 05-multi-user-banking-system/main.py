from utils import (
    generate_account_number,
    validate_account_number,
    get_valid_amount,
    record_transaction,
    display_transactions
)

accounts = {}


def create_account():
    name = input("Enter account holder name: ").strip()

    if not name:
        print("❌ Name cannot be empty.")
        return

    acc_number = generate_account_number(accounts)

    accounts[acc_number] = {
        "name": name,
        "balance": 0.0,
        "transactions": []
    }

    print(f"✅ Account created successfully.")
    print(f"🔑 Account Number: {acc_number}")


def deposit_money():
    acc_number = input("Enter account number: ").strip().upper()

    if not validate_account_number(accounts, acc_number):
        print("❌ Invalid account number.")
        return

    amount = get_valid_amount("Enter deposit amount: ")

    account = accounts[acc_number]
    account["balance"] += amount

    record_transaction(account, "deposit", amount)

    print(f"✅ Deposited ₹{amount}. Current Balance: ₹{account['balance']}")


def withdraw_money():
    acc_number = input("Enter account number: ").strip().upper()

    if not validate_account_number(accounts, acc_number):
        print("❌ Invalid account number.")
        return

    account = accounts[acc_number]
    amount = get_valid_amount("Enter withdrawal amount: ")

    if amount > account["balance"]:
        print("❌ Insufficient balance.")
        return

    account["balance"] -= amount
    record_transaction(account, "withdraw", amount)

    print(f"✅ Withdrawn ₹{amount}. Current Balance: ₹{account['balance']}")


def check_balance():
    acc_number = input("Enter account number: ").strip().upper()

    if not validate_account_number(accounts, acc_number):
        print("❌ Invalid account number.")
        return

    account = accounts[acc_number]
    print(f"💰 Current Balance: ₹{account['balance']}")


def show_transactions():
    acc_number = input("Enter account number: ").strip().upper()

    if not validate_account_number(accounts, acc_number):
        print("❌ Invalid account number.")
        return

    display_transactions(accounts[acc_number]["transactions"])


def show_menu():
    print("\n🏦 Banking System")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Transaction History")
    print("6. Exit")


while True:
    show_menu()

    try:
        choice = int(input("Enter choice (1-6): "))

        if choice == 6:
            print("👋 Exiting Banking System")
            break
        elif choice == 1:
            create_account()
        elif choice == 2:
            deposit_money()
        elif choice == 3:
            withdraw_money()
        elif choice == 4:
            check_balance()
        elif choice == 5:
            show_transactions()
        else:
            print("❌ Invalid choice.")

    except ValueError:
        print("❌ Please enter a numeric choice.")
