from random import *
from datetime import date, timedelta
from src.utils.validation_utility import get_valid_input, validate_positive_int, CancelInput

def generate_test_transactions(transactions: list[dict[str, any]]) -> list[dict[str, any]]:
    """
    Create test financial transactions.
    Csv headers should be 'transaction_id', 'date', 'customer_id', 'amount', 'type', 'description'. In that order.
    Data types should be positive int, datetime.date in format YYYY-MM-DD, int, positive float,
      string in ('debit', 'credit', 'transfer'), string. In that order.
    """
    print("Enter 'c' to cancel and go back to main menu.")
    while True:
        try:
            # Get number of transactions to create from user
            number_of_transactions = get_valid_input("How many test transactions would you like to generate? ", validate_positive_int)          
            # If transactions already has data, clear it
            transactions.clear()
            # Get date range for random creation
            start_date = date(1989, 1, 1)
            end_date = date.today()
            difference = end_date - start_date
            # Create specified number of transactions with random data
            for i in range(number_of_transactions):
                test_transaction = {
                    'transaction_id': i + 1,
                    'date': start_date + timedelta(days=randint(0, difference.days)),
                    'customer_id': randint(1, 999),
                    'amount': round(uniform(0.01, 9999999.99), 2),
                    'type': choice(['debit', 'credit', 'transfer']),
                }
                test_transaction['description'] = f"Customer {test_transaction['customer_id']} logged a {test_transaction['type']} for {test_transaction['amount']}."
                transactions.append(test_transaction)
            print("\nTest transactions generated!")
        # Catch user cancellation
        except CancelInput as e:
            print(e)
        return transactions
