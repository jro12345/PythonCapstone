import os
from datetime import datetime
from src.transaction_viewer import format_transactions_table
from src.utils.helpers import cleanup_old_files

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

def create_report_statement(transactions: list[dict[str, any]]) -> str:
    """ Creates a string statements formatted with totals based on transaction type """
    # Sum the totals
    sums = get_sums_by_type(transactions)
    calculated_totals = (
    "Financial Summary:\n"
    f"Total Credits: ${sums['credit']:.2f}\n"
    f"Total Debits: ${sums['debit']:.2f}\n"
    f"Total Transfers: ${sums['transfer']:.2f}\n"
    f"Net Balance: ${(sums['credit'] - sums['debit']):.2f}\n"
    "By type:\n"
    f"  Credit: ${sums['credit']:.2f}\n"
    f"  Debit: ${sums['debit']:.2f}\n"
    f"  Transfer: ${sums['transfer']:.2f}"
    )
    return calculated_totals

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

def customer_totals_lines(transactions: list[dict[str, any]]) -> str:
    """ Builds and returns a string containing customer's transaction totals. """
    # Get customer totals by customer id
    customer_totals = calculate_customer_totals(transactions)
    # Build list of customer totals ready to print
    customer_lines = [f"Customer ID: {cid}: ${total:.2f}" for cid, total in sorted(customer_totals.items())]
    # Join header with customer totals lines
    customer_summary = "Customer Totals:\n" + '\n'.join(customer_lines)
    return customer_summary

def sorted_transactions_lines(transactions: list[dict[str, any]]) -> str:
    """ Builds and returns a table containing transactions sorted by date. """
    # Sort transactions by date
    sorted_transactions = sorted(transactions, key=lambda txn: txn['date'])
    # Format transactions into a table
    sorted_transaction_lines = format_transactions_table(sorted_transactions)
    return sorted_transaction_lines

def analyze_finances(transactions: list[dict[str, any]], filename: str = 'analysis.txt') -> None:
    """ 
    Prints a string formatted with totals based on transaction type.
    Writes analysis to file.
    """
    analysis = create_report_statement(transactions)
    print(analysis)
    try:
        with open(filename, 'w', encoding='utf-8') as analysis_file:
            analysis_file.write(analysis)
    except Exception as e:
        print(f"\nThere was a problem generating your analysis file, {e}\n")

def get_customer_with_highest_debit():
    print()

def generate_report(transactions: list[dict[str, any]], filename: str ='report.txt') -> None:
    """ Creates a new file containing transaction totals based on type. """
    try:   
        # Build report output
        output = '\n'.join([
            "FINANCIAL ANALYSIS REPORT",
            '*' * 40,
            create_report_statement(transactions),
            '*' * 40,
            "Transaction totals by customer:",
            customer_totals_lines(transactions),
            '*' * 40,
            "Transactions sorted by date:",
            sorted_transactions_lines(transactions)
        ])
        # Write to file
        cleanup_old_files(filename, "report")
        report_filename = f"{os.path.splitext(filename)[0]}_{datetime.now().strftime("%Y%m%d")}.txt"
        with open(report_filename, 'w', encoding='utf-8') as report:
            report.write(output)
        print("Report Generated!")
    except Exception as e:
        print(f"\nThere was a problem generating your report file, {e}\n")