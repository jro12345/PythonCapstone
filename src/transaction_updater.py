import src.utils.helpers as helpers
import src.utils.validation_utility as validation_utility
from src.utils.table_formatting import numbered_transaction_table

def get_field_to_update() -> str:
    """
    Prompt user for transaction field to update.
    If valid field is entered, returns.
    If invalid field is entered, throws error and prompts again. """
    valid_fields = ["description", "type", "amount"]
    while True:
        try:
            update_field = input("Change which field? (description, type, amount): ").strip().lower()
            if update_field not in valid_fields:
                raise ValueError(f"\nYou did not enter a valid field: '{update_field}'. The fields you can update are: {valid_fields}.\n")
            return update_field
        except ValueError as e:
            print(e)

def get_updated_field_value(update_field: str) -> any:
    """
    Prompt user for new transaction field value.
    Depending on field, validates accordingly. 
    If valid value is entered, returns.
    If invalid field is entered, throws error and prompts again. """
    while True:
        try:
            updated_value = input(f"New {update_field}: ").strip()
            # If 'description', return. 'description' can be any value.
            if update_field == "description":
                pass
            # Call validation functions based on update_field
            elif update_field == "type":
                updated_value = validation_utility.validate_transaction_type(updated_value)              
            elif update_field == "amount":
                updated_value = validation_utility.validate_amount(updated_value)
            # Handle edge case where 'update_field' is not in updatable fields
            else:
                raise ValueError(f"\nYou shouldn't be here. You cannot change this field!\n")
            return updated_value
        except ValueError as e:
            print(e)

def update_transaction_by_id(transaction_id: int, update_field: str, updated_value: str, transactions: list[dict[str,any]]) -> list[dict[str,any]]:
    """ Update transaction by id. """
    updated = True
    for transaction in transactions:
        # If found transaction id in transactions, update that transaction
        if transaction['transaction_id'] == transaction_id:
            transaction[update_field] = updated_value
            # If type, change amount accordingly
            if update_field == 'type':
                transaction['amount'] = -abs(transaction['amount']) if updated_value == 'debit' else abs(transaction['amount'])
            # If updating amount and type is debit, make amount negative
            elif update_field == 'amount' and transaction['type'] == 'debit':
                transaction['amount'] = -updated_value
            updated = True
    if updated:
        print("\nTransaction updated!")
    else:
        print(f"\nNo transaction id matching {transaction_id} foudn to update")
    return transactions

def update_transactions(transactions: list[dict[str, any]]) -> list[dict[str, any]]:
        """
        Prints a numbered table view of transactions.
        Prompts user to select from numbered ids.
        Prompts user for field to update.
        Prompts user for new field value.
        Updates field with new value in transactions.
        Returns transactions.
        """
        # Print numbered table view
        numbered_transaction_table(transactions)
        # Get transaction to delete from user by id
        transaction_id = helpers.get_transaction_id_to_modfy(transactions)
        # Get field to update from user
        update_field = get_field_to_update()
        # Get new value for field to update from user
        updated_value = get_updated_field_value(update_field)
        # Modify update field value in transaction with matching id and return new transactions list
        return update_transaction_by_id(transaction_id, update_field, updated_value, transactions)
    
