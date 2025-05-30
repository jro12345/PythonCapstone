import os
from src.utils.validation_utility import validate_transaction_id

def get_transaction_id_to_modfy(transactions: list[dict[str, any]]) -> int:
    """ Prompt user for an id in transactions list and validates it. Returns Error or valid id. """
    while True:
        try:
            transaction_ids = []
            # Gets all transaction ids in transactions
            transaction_ids.extend(transaction['transaction_id'] for transaction in transactions)
            min_id = min(transaction_ids) # Smallest id for user prompt
            max_id = max(transaction_ids) # Lrgest id for user prompt
            # Prompts user for transaction id
            modify_row_id = validate_transaction_id(input(f"Select transaction {min_id}-{max_id}: ").strip())
            # Throw error if user input is not in transaction ids
            if modify_row_id not in transaction_ids:
                raise ValueError("\nThe number you entered does not exist in transaction_ids\n")
            # Return valid transaction id
            return modify_row_id
        # Handle errors and prompt again             
        except ValueError as e:
            print(f"\nYou must enter a valid transaction number, {e}\n")

def cleanup_old_files(original_filename: str, type_of_file: str) -> None:
    """
    Clean up old files before writing new ones.
    User specifices which type of files to cleanup.
    This is intended to be used for old reports and old backup files
    """
    # Get base name of file
    base_filename = os.path.splitext(original_filename)[0]
    if type_of_file == "backup":
        file_prefix = f"{base_filename}_backup_"
        file_suffix = ".csv"
    else:
        file_prefix = base_filename
        file_suffix = ".txt"
    # Find files matching pattern
    old_files = [
        f for f in os.listdir(".")
        if f.startswith(file_prefix) and f.endswith(file_suffix)
    ]
    # Delete old files
    for file in old_files:
        os.remove(file)
    print(f"Old {type_of_file}s have been cleaned up.")