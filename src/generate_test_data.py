from random import *
from datetime import datetime, timedelta

def generate_test_transactions() -> list[dict[str, any]]:
    """
    Create test financial transactions.
    Csv headers should be 'transaction_id', 'date', 'customer_id', 'amount', 'type', 'description'. In that order.
    Data types should be positive int, datetime.date in format YYYY-MM-DD, int, positive float,
      string in ('debit', 'credit', 'transfer'), string. In that order.
    """
    transactions = []
    while True:
        try:
            # Get number of transactions to create from user
            number_of_transactions = input("How many test transactions would you like to generate? ").strip()
            # Validate input
            if not number_of_transactions.isdigit():
                raise ValueError(f"You must generate a positive number of transactions")
            number_of_transactions = int(number_of_transactions)
            if number_of_transactions <=0:
                raise ValueError("You must generate a positive number of transactions")
            # Get date range for random creation
            start_date = datetime(1989, 1, 1).date()
            end_date = datetime(datetime.now().year, datetime.now().month, datetime.now().day).date()
            difference = end_date - start_date
            # Create number of transactions with random data
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
            return transactions
        except Exception as e:
            print(e)
