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
        try:
            # Get type filter from user
            type_to_view = input("Which type of transaction would you like to view?\n(debit/credit/transfer): ").strip().lower()
            if type_to_view not in ['debit', 'credit', 'transfer']:
                raise ValueError(f"\nType can only be 'debit', 'credit', or 'transfer', you chose {type_to_view}\n")
            # Filter transactions
            filtered_transactions = [txn for txn in transactions if txn['type'] == type_to_view]
            # Print table in formatted view
            print('\n', format_transactions_table(filtered_transactions))
            break
        except ValueError as e:
            print(e)

def view_transactions(transactions: list[dict[str, any]]) -> None:
    """
    View transactions.
    Depending on user input, all transactions will be displayed or just certain types of transactions.
    """
    while True:
        try:
            # Prompt user for how to filter transactions
            view_by_type = input("Do you want to view transactions by a certain type?\n('yes' to filter 'no' to view all): ").strip().lower()
            if view_by_type not in ['yes', 'no']:
                raise ValueError(f"\nYou must enter yes or no, you entered {view_by_type}\n")
            # Print all transactions
            elif view_by_type == 'no':
                print('\n', format_transactions_table(transactions))
                break
            # Print only specific types of transactions
            elif view_by_type == 'yes':
                view_transactions_by_type(transactions)
                return                
        except ValueError as e:
            print(e)