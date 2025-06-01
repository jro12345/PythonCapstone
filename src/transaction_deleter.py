import src.utils.helpers as helpers
import src.utils.table_formatting as formatting_helper
from src.utils.validation_utility import get_valid_input, validate_yes_no, CancelInput

def delete_transaction_by_id(transaction_id: int, transactions: list[dict[str, any]]) -> list[dict[str,any]]:
    """ Delete transaction by id.
        Prompts user for certainty and prints selected row.
        Does nothing if certainty is 'no'.
        Deletes transaction if certainty is 'yes.   
    """
    deleted = False
    for i, transaction in enumerate(transactions):
        if transaction['transaction_id'] == transaction_id:
            try:
                print(f"Are you sure you want to delete transaction?\n{transaction}")
                certain = get_valid_input("yes/no: ", validate_yes_no)
                if certain == 'no':
                    print("\nMake up your mind.")
                    return transactions
                else:
                    transactions.pop(i)
                    deleted = True
                    break
            except ValueError as e:
                print(e)
    if deleted:
        print("\nTransaction deleted!")
    else:
        print(f"\nNo transaction id found matching {transaction_id} to delete!")
    return transactions

def delete_transaction(transactions: list[dict[str, any]]) -> list[dict[str, any]]:
    """
    Prints a numbered table view of transactions.
    Prompts user to select from numbered ids to delete.
    Prompts user for certainty of deletion.
    Deletes selected transaction if certainty is 'yes'.
    Does nothing if certainty is 'no'.
    Returns transactions.
    """
    # Print numbered table view
    formatting_helper.numbered_transaction_table(transactions)
    print("Enter 'c' at any step to cancel and go back to main menu")
    try:
        # Get transaction to delete from user by id
        delete_id = helpers.get_transaction_id_to_modfy(transactions)
        # Delete transaction with matching transaction id and return new transactions list
        return delete_transaction_by_id(delete_id, transactions)
    except CancelInput as e:
        print(e)
        return transactions



