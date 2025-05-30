from src.utils.validation_utility import *
        
def add_transaction(transactions: list[dict[str, any]]) -> list[dict[str, any]]:
    """ Creates a new transaction based on user input and adds it to transactions. """
    # Call input and validation functions based on transaction values in order to create new transaction
    if not transactions:
        print("Transactions list is empty.\n")
    transaction_id = max(transaction['transaction_id'] for transaction in transactions) + 1 if transactions else 1
    date = get_valid_date()
    customer_id = get_valid_customer_id()
    amount = get_valid_amount()
    type = get_valid_type()
    if type == 'debit':
        amount = -amount
    description = input("Enter description: ")
    
    transaction_input = {
        'transaction_id': transaction_id,
        'date': date,
        'customer_id': customer_id,
        'amount': amount,
        'type': type,
        'description': description
    } 
    # Add new transaction to transactions
    transactions.append(transaction_input)
    print("\nTransaction Added!")
    return transactions
