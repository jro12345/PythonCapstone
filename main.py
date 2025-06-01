from sys import exit
from src.transaction_adder import add_transaction
from src.transaction_deleter import delete_transaction
from src.analyze_and_report import analyze_finances, generate_report
from src.transaction_saver import save_transactions
from src.transaction_loader import load_transactions
from src.transaction_viewer import view_transactions
from src.transaction_updater import update_transactions
from src.utils.validation_utility import validate_transactions_loaded
from src.generate_test_data import generate_test_transactions


def main():
    transactions = []
    try:
        while True:
            print("\nSmart Personal Finance Analyzer")
            print("0. Generate test transactions")
            print("1. Load Transactions")
            print("2. Add Transaction")
            print("3. View Transactions")
            print("4. Update Transaction")
            print("5. Delete Transaction")
            print("6. Analyze Finances")
            print("7. Save Transactions")
            print("8. Generate Report")
            print("9. Exit (At any time you may press ctrl+c to exit)")
            choice = input("Select an option: ").strip()
            print()
            # Call functions based on choice
            if choice == '0':
                transactions = generate_test_transactions(transactions)
            elif choice == '1':
                transactions = load_transactions()
            elif choice == '2':
                transactions = add_transaction(transactions)
            elif choice == '3':
                if validate_transactions_loaded(transactions):
                    view_transactions(transactions)
            elif choice == '4':
                if validate_transactions_loaded(transactions):
                    transactions = update_transactions(transactions)
            elif choice == '5':
                if validate_transactions_loaded(transactions):
                    transactions = delete_transaction(transactions)
            elif choice == '6':
                if validate_transactions_loaded(transactions):
                    analyze_finances(transactions)
            elif choice == '7':
                if validate_transactions_loaded(transactions):
                    save_transactions(transactions)
            elif choice == '8':
                if validate_transactions_loaded(transactions):
                    generate_report(transactions)
            elif choice == '9':
                print("\nExiting program\n")
                break
            else:
                print("Please select a valid number from the list")
    # Exit program if 'ctrl+c' is entered
    except KeyboardInterrupt:
        print("\n")
        print("Exiting program\n")
        exit(0)
        
if __name__ == '__main__':
    main()