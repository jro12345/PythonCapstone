from src.utils.validation_utility import *

class NoTransactionsToDisplayError(Exception):
    """ Custom exception for when certain transactions types do not exist in file. """
    def __init__(self, transaction_type: str):
        message = f"\nThere are no {transaction_type} transactions in this file"
        super().__init__(message)

def format_transactions_table(transactions: list[dict[str, any]]) -> str:
    """
    Prints transactions with columns names.
    Formatted into a table view with column separators. 
    """
    # Column names and csv header header values
    column_names = [
        ("ID", "transaction_id"),
        ("Date", "date"),
        ("Customer", "customer_id"),
        ("Amount", "amount"),
        ("Type", "type"),
        ("Description", "description")
    ]
    columns = []
    # Loop through column names
    for display_name, key in column_names:
        # Get length of column name
        header_len = len(display_name)
        # Get max length of all values in column
        value_len = max(len(str(transaction.get(key, ''))) for transaction in transactions)
        # Get max length of header and value, add 2 to max length for column padding
        column_width = max(header_len, value_len) + 2
        # Append length as max to column names list
        columns.append((display_name, column_width, key))
    # Create formatted table header
    header = '|'.join(f" {name:<{width}}" for name, width, _ in columns)
    # Print row to separate header from values
    separator = '-' * len(header)
    # Print rows of formatted table data
    rows = []
    for transaction in transactions: 
        # Create formatted data row based on transaction values     
        line = '|'.join(
        f" {f'{transaction[key]:.2f}' if key == 'amount' else str(transaction[key]):<{width}}"
        for _, width, key in columns
    )
        rows.append(line)
    # Build table
    table = '\n'.join([
        header,
        separator,
        *rows
    ])
    return table

def view_transactions_by_type(transactions: list[dict[str, any]]) -> None:
    """ Filter transactions by type and print in formatted view. """
    while True:
        # Get type to filter on
        type_to_view = get_valid_input("Which type of transaction would you like to view?\n(debit/credit/transfer): ", validate_transaction_type)
        # Filter transactions by specified type
        filtered_transactions = [txn for txn in transactions if txn['type'] == type_to_view]
        # If no transactions for specified type, raise error
        if not filtered_transactions:
            raise NoTransactionsToDisplayError(type_to_view)
        # Print table in formatted view
        print('\n', format_transactions_table(filtered_transactions))
        return

def view_transactions(transactions: list[dict[str, any]]) -> None:
    """
    View transactions.
    Depending on user input, all transactions will be displayed or just certain types of transactions.
    """
    while True:
        try:
            print("Enter 'c' to cancel and go back to main menu")
            # Prompt user for how to filter transactions
            view_by_type = get_valid_input("Do you want to view transactions by a certain type?\n('yes' to filter 'no' to view all): ", validate_yes_no)
            # Print all transactions
            if view_by_type == 'no':
                print('\n', format_transactions_table(transactions))
                break
            # Print only specific types of transactions
            if view_by_type == 'yes':
                view_transactions_by_type(transactions)
                break 
        # Catch case where no transactions to display by type. Reprompt user to view transations
        except NoTransactionsToDisplayError as e:
            print(f"{e}\nPlease try another type or view all transactions\n")
            continue               
        # Catch user cancellelation
        except CancelInput as e:
            print(e)
            return