import os
from datetime import datetime
from src.transaction_viewer import format_transactions_table
from src.utils.helpers import cleanup_old_files
from src.utils.validation_utility import get_valid_input, validate_yes_no, CancelInput

def get_sums_by_type(transactions: list[dict[str, any]]) -> dict:
    """
    Calculates the sums of the transaction types.
    Returns a dictionary containing the sums {type: sum}.
    If type does not exist in transactions, defaults to 0.
    """
    sums_by_type = {
        'credit': float(0),
        'debit': float(0),
        'transfer': float(0)
    }
    for transaction in transactions:
        abs_amount = float(abs(transaction['amount']))
        sums_by_type[transaction['type']] += abs_amount
    return sums_by_type

def analyze_transactions_by_year(transactions: list[dict[str, any]]) -> list[dict[str, any]]:
    """
    Ask user if they want to analyze transactions by year.
    If no, return orginal transaction list.
    If yes, return only transactions for the specified year.
    """
    print("Enter 'c' at any step to cancel and go back to main menu")
    specify_year = get_valid_input("Do you want to analyze transactions for a specific year (yes/no?: ", validate_yes_no)
    if specify_year == "no":
        return 'All', transactions
    else:
        # Get list of all years in transactions
        valid_years = {int(datetime.strftime(txn['date'], "%Y")) for txn in transactions}
        while True:                  
            year_input = input(f"Which year would you like to analyze?:\nValid years are {sorted(valid_years)}: ").strip()
            if year_input == 'c':
                raise CancelInput
            # Validate year input against available years in transactions
            elif year_input not in [str(year) for year in valid_years]:
                print(f"\nYou must select a valid year from {sorted(valid_years)}\n")
            else:
                # Return only transactions for the year specified
                return year_input, [txn for txn in transactions if txn['date'].year == int(year_input)]
                
def create_report_statement(year: str, transactions: list[dict[str, any]]) -> str:
    """ Creates a string statements formatted with totals based on transaction type """
    # Sum the totals
    sums = get_sums_by_type(transactions)
    financial_summary = '\n'.join([
    f"Financial Summary: Year ({year})",
    f"Total Credits: ${sums['credit']:.2f}",
    f"Total Debits: ${sums['debit']:.2f}",
    f"Total Transfers: ${sums['transfer']:.2f}",
    f"Net Balance: ${(sums['credit'] - sums['debit']):.2f}",
    "By type:",
    f"  Credit: ${sums['credit']:.2f}",
    f"  Debit: ${sums['debit']:.2f}",
    f"  Transfer: ${sums['transfer']:.2f}"
    ])
    return financial_summary

def calculate_customer_totals(transactions: list[dict[str, any]]) -> dict[int, float]:
    """ Calculates total transaction amounts per customer using a set. """
    # Get unique customer ids
    customer_ids = {txn['customer_id'] for txn in transactions}
    # Initialize tuple for each customer id, defaulting total to 0
    totals = {cid: 0.0 for cid in customer_ids}
    # Sum totals for customers
    for txn in transactions:
        totals[txn['customer_id']] += txn['amount']
    return totals

def calculate_percentage_of_type_totals(transactions: list[dict[str, any]]) -> str:
    """
    Calculates the percentage of total transactions by type.
    Returns a string listing out the total of transactions, total by type, and percentage of total by type.
    """
    type_totals = {
        'debit': 0.0,
        'credit': 0.0,
        'transfer': 0.0
        }
    percentage_of_total = {
        'debit': 0.0,
        'credit': 0.0,
        'transfer': 0.0
        }
    # Get type totals
    for txn in transactions:
        type_totals[txn['type']] += abs(txn['amount'])
    # Get overall total
    overall_total = sum(type_totals.values())
    if overall_total > 0:
        # Get total percentage by type
        for txn_type in type_totals:
            percentage_of_total[txn_type] = round((type_totals[txn_type] / overall_total) * 100, 2)
    return '\n'.join([
        f"The overall total for transactions is ${overall_total}",
        f"Total debits are ${type_totals['debit']:.2f}, which makes up {percentage_of_total['debit']}% of total transactions",
        f"Total credits are ${type_totals['credit']:.2f}, which make up {percentage_of_total['credit']}% of total transactions",
        f"Total Transfers are ${type_totals['transfer']:.2f}, which make up {percentage_of_total['transfer']}% of total transactions"
    ])
    
def customer_totals_lines(transactions: list[dict[str, any]]) -> str:
    """ Builds and returns a string containing customer's transaction totals. """
    # Get customer totals by customer id
    customer_totals = calculate_customer_totals(transactions)
    # Build list of customer totals ready to print
    customer_lines = [f"Customer ID: {cid}: ${total:.2f}" for cid, total in sorted(customer_totals.items())]
    # Join header with customer totals lines
    customer_summary = "Customer Totals:\n" + '\n'.join(customer_lines)
    return customer_summary

def date_sorted_transactions_lines(transactions: list[dict[str, any]]) -> str:
    """ Builds and returns a table containing transactions sorted by date. """
    # Sort transactions by date
    sorted_transactions = sorted(transactions, key=lambda txn: txn['date'])
    # Format transactions into a table
    sorted_transaction_lines = format_transactions_table(sorted_transactions)
    return sorted_transaction_lines

def get_customers_with_highest_transactions(transactions: list[dict[str, any]]) -> str:
    """
    Calulates highest transactions based on type.
    Returns a string containing customer id and max transaction per type.
    """
    lines = []
    highest_transactions = {
        'debit': None,
        'credit': None,
        'transfer': None
    }
    max_amounts = {
        'debit': float('-inf'),
        'credit': float('-inf'),
        'transfer': float('-inf')
    }
    # Gets transaction containing max transaction per type
    for txn in transactions:
        txn_type = txn['type']
        amount = abs(txn['amount'])
        if amount > max_amounts[txn_type]:
            max_amounts[txn_type] = amount
            highest_transactions[txn_type] = txn
    # Appends string listing highest transaction per type along with customer id associated
    for txn_type in highest_transactions:
        if highest_transactions[txn_type]:
            lines.append(f"Highest {txn_type} was Customer Id {highest_transactions[txn_type]['customer_id']}: ${max_amounts[txn_type]:.2f}")
        # Appends string if no transaction was found for the given type
        else:
            lines.append(f"There were no {txn_type} transactions in this file")
    return '\n'.join(lines)

def get_transaction_date_range(transactions: list[dict[str, any]]) -> str:
    start_date = min(transactions, key=lambda txn: txn['date'])['date']
    end_date = max(transactions, key=lambda txn: txn['date'])['date']
    return f"{start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}"

def analyze_finances(transactions: list[dict[str, any]], filename: str = 'analysis.txt') -> None:
    """ 
    Prints a string formatted with totals based on transaction type.
    Writes analysis to file.
    """
    try:
        year, transactions_by_year = analyze_transactions_by_year(transactions)
        analysis = create_report_statement(year, transactions_by_year)
        print(analysis)
        try:
            with open(filename, 'w', encoding='utf-8') as analysis_file:
                analysis_file.write(analysis)
        except Exception as e:
            print(f"\nThere was a problem generating your analysis file, {e}\n")
    except CancelInput as e:
        print(e)

def generate_report(transactions: list[dict[str, any]], filename: str ='report.txt') -> None:
    """ Creates a new file containing transaction totals based on type. """
    try:   
        # Build report output
        output = '\n'.join([
            'FINANCIAL ANALYSIS REPORT',
            f'Report contains dates from {get_transaction_date_range(transactions)}',
            '*' * 40,
            create_report_statement('All', transactions),
            '*' * 40,
            'Percentage of total by type:',
            calculate_percentage_of_type_totals(transactions),
            '*' * 40,
            "Customers with highest transactions:",
            get_customers_with_highest_transactions(transactions),
            '*' * 40,
            'Transaction totals by customer:',
            customer_totals_lines(transactions),
            '*' * 40,
            'Transactions sorted by date:',
            date_sorted_transactions_lines(transactions)
        ])
        # Cleanup old report files
        cleanup_old_files(filename, "report")
        # Timestamp report filename
        report_filename = f"{os.path.splitext(filename)[0]}_{datetime.now().strftime("%Y%m%d")}.txt"
        # Write report
        with open(report_filename, 'w', encoding='utf-8') as report:
            report.write(output)
        print("Report Generated!")
    except Exception as e:
        print(f"\nThere was a problem generating your report file, {e}\n")