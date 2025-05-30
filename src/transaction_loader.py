import csv
from src.utils.validation_utility import *

def log_error(message: str, log_file: str = 'error_log.txt') -> None:
    try:
        with open(log_file, 'a', encoding='utf-8') as error_file:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            error_file.write(f"{timestamp} - ERROR - {message}\n")
            print(message)
    except Exception as e:
        print(f"Failed to write to {log_file}: {e}")
        
def load_transactions(filename: str='financial_transactions.csv') -> list[dict[str, any]]:
    """
    Reads from csv (filename).
    Validates all headers and fields:
    Csv headers should be 'transaction_id', 'date', 'customer_id', 'amount', 'type', 'description'. In that order.
    Data types should be positive int, datetime.date in format YYYY-MM-DD, int, positive float,
      string in ('debit', 'credit', 'transfer'), string. In that order.
    Throws error if either of those are not true or file is not found.
    Will skip row if a row's datatypes are not valid. 
    Returns list of transaction dictionaries.
    """
    transactions = []
    expected_headers = ["transaction_id", "date", "customer_id", "amount", "type", "description"]
    transaction_ids = []
    try:
        
        # Open and read csv file
        with open(filename, 'r', encoding='utf-8') as csv_file:
            transaction_counter = 0
            reader = csv.reader(csv_file)
            # Split first row for valid header check
            first_row = csv_file.readline().strip().split(',')
            # Reset file reader location
            csv_file.seek(0) 
            # Check if first row matches expected headers
            has_headers = first_row == expected_headers
            # If valid headers skip first row
            if has_headers:
                reader = csv.DictReader(csv_file)
            # If invalid headers used, try to load all rows as data
            else:
                print("No valid headers found, first row of file will be treated as data.")
                reader = csv.DictReader(csv_file, fieldnames=expected_headers)
            for line in reader:
                try:
                    transaction_id = validate_transaction_id(line['transaction_id'], transaction_ids)
                    date = validate_date(line['date'])
                    customer_id = validate_customer_id(line['customer_id'])
                    transaction_type = validate_transaction_type(line['type'])
                    amount = -validate_amount(line['amount']) if transaction_type == "debit" else validate_amount(line['amount'])
                    description = line['description']
                    validated_transaction = {
                        'transaction_id': transaction_id,
                        'date': date,
                        'customer_id': customer_id,
                        'amount': amount,
                        'type': transaction_type,
                        'description': description
                    }
                    # Add row to transactions list
                    transactions.append(validated_transaction)
                    transaction_counter += 1
                    # Add transaction id to list to keep track of uniqueness
                    transaction_ids.append(transaction_id)
                # Skip invalid rows
                except ValueError as e:
                    log_error(f"Skipping invalid row:\n{line}{e}")
        if len(transactions) != 0:
            print(f"\n{transaction_counter} transactions loaded!")
        else:
            print("\nFile loaded but transactions list is empty!")
        return transactions
    except FileNotFoundError:
        log_error(f"\n{filename} was not found. Please upload file and try again.\n")
    except Exception as e:
        log_error(f"\nSomething went wrong with loading file, {e}\n")