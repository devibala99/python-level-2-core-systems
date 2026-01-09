def generate_account_number(accounts):
    """
    Generate a unique account number in the format ACC1001, ACC1002, ...
    """
    if not accounts:
        return "ACC1001"

    last_number = max(int(acc[3:]) for acc in accounts.keys())
    return f"ACC{last_number + 1}"


def validate_account_number(accounts, account_number):
    """
    Validate whether the given account number exists.
    """
    return account_number in accounts


def get_valid_amount(prompt):
    """
    Prompt user for a positive numeric amount.
    Returns a valid float amount.
    """
    while True:
        try:
            amount = float(input(prompt))
            if amount <= 0:
                print("❌ Amount must be greater than zero.")
                continue
            return amount
        except ValueError:
            print("❌ Invalid input. Enter a numeric value.")


def record_transaction(account, tx_type, amount):
    """
    Record a transaction into the account's transaction history.

    Transaction format:
    {
        "type": "deposit" | "withdraw",
        "amount": amount,
        "balance_after": updated_balance
    }
    """
    transaction = {
        "type": tx_type,
        "amount": amount,
        "balance_after": account["balance"]
    }

    account["transactions"].append(transaction)


def display_transactions(transactions):
    """
    Display transaction history in a readable format.
    """
    if not transactions:
        print("📭 No transactions found.")
        return

    print("\n📄 Transaction History")
    print("-" * 30)

    for index, txn in enumerate(transactions, start=1):
        print(f"{index}. Type: {txn['type'].capitalize()}")
        print(f"   Amount: {txn['amount']}")
        print(f"   Balance After: {txn['balance_after']}")
        print("-" * 30)
