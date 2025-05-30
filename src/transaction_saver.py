import csv
import os
from datetime import datetime
from src.utils.helpers import cleanup_old_files

def backup_transactions_file(original_filename: str) -> None:
    try:
        if not os.path.exists(original_filename):
            print(f"{original_filename} does not exist in order to back it up.")
        cleanup_old_files(original_filename, "backup")
        backup_filename = f"{os.path.splitext(original_filename)[0]}_backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv"
        os.rename(original_filename, backup_filename)
        print(f"{original_filename} has been backed up: {backup_filename}")
    except Exception as e:
        print(e)


def save_transactions(transactions: list[dict[str, any]], filename: str='financial_transactions.csv') -> None:
    """ Write transactions to a csv file. """
    try:
        backup_transactions_file(filename)
        # Open file and write headers
        with open(filename, 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=transactions[0].keys())
            writer.writeheader()
            # Write rows
            for transaction in transactions:
                # Create a copy of the transaction with formatted amount for CSV writing
                row = transaction.copy()
                row['amount'] = f"{abs(transaction['amount']):.2f}"
                writer.writerow(row)
        print(f"Transactions saved to {filename}") 
    except Exception as e:
        print(f"\nError encountered while saving file, {e}\n")
