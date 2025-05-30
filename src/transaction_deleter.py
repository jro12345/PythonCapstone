import src.utils.helpers as helpers
import src.utils.table_formatting as formatting_helper

def certainty_check(transaction: dict[str,any]) -> bool:
    """
    Prompts user for 'yes'/'no'.
    Throws error and prompts again if input does not match one of those.
    Returns True for 'yes' and False for 'no'.
    """
    while True:
        try:
            certain = input(f"Are you sure you want to delete transaction?\n{transaction}\nyes/no: ").strip().lower()
            if certain not in ["yes", "no"]:
                raise ValueError(f"You must enter yes or no, you entered {certain}")
            if certain == "no":
                print("\nMake up your mind.")
                return False
            return True
        except ValueError as e:
            print(e)

def delete_transaction_by_id(transaction_id: int, transactions: list[dict[str, any]]) -> list[dict[str,any]]:
    """ Delete transaction by id.
        Prompts user for certainty and prints selected row.
        Does nothing if certainty is 'no'.
        Deletes transaction if certainty is 'yes.   
    """
    deleted = False
    for i, transaction in enumerate(transactions):
        if transaction['transaction_id'] == transaction_id:
            while True:
                try:
                    certain = input(f"Are you sure you want to delete transaction?\n{transaction}\nyes/no: ").strip().lower()
                    if certain not in ['yes', 'no']:
                        raise ValueError(f"You must enter yes or no, you entered {certain}")
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
    # Get transaction to delete from user by id
    delete_id = helpers.get_transaction_id_to_modfy(transactions)
    # Delete transaction with matching transaction id and return new transactions list
    return delete_transaction_by_id(delete_id, transactions)



