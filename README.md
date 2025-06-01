# Finanical Analyzer
Financial Analyzer is a Python-based command-line tool for managing and analyzing financial data. It allows users to load, add, view, update, save and report on financial transactions. Users can also generate randomized test data to work with. This project was designed with robust input validation and error handling, making it suitable for personal finance tracking. 
## Installation
Follow these steps to set up and run FinancialAnalyzer on your local machine:
1. **Clone the Repository**:
   Clone the project from GitHub to your local machine:
   ```bash
   git clone https://github.com/Jro123456/FinancialAnalyzer.git
   cd FinancialAnalyzer
2. Install Python: Ensure Python 3.8 or higher is installed. You can download it from python.org
3. Dependencies: This program uses only standard Python libraries.
4. Run the Application:
   ```bash
   financial_analyzer.py
5. Verify Setup:
   Program should display the main menu:
   ```
    Smart Personal Finance Analyzer
    0. Generate Test Transactions
    1. Load Transactions
    2. Add Transaction
    3. View Transactions
    4. Update Transaction
    5. Delete Transaction
    6. Analyze Finances
    7. Save Transactions
    8. Generate Report
    9. Exit (At any time you may press ctrl+c to exit)
    Select an option:
## Financial Data Structure
CSV format with headers: transaction_id, date, customer_id, amount, type, description  
transaction_id: Unique ID consisting of positive ints  
date: YYYY-MM-DD format  
customer_id: positive int  
amount:  positive float (debits will be made negative programmatically)  
type: (debit, credit, or transfer)'
description: string description of the transaction
## Features
 - Generate Test Transaction Data: Load randomized data in valid format.
 - Load Transactions: Load transactional data from a csv file.
 - Add Transactions: Input custom transactions. Program handles all field validations in order to ensure correct data structure.
 - View Transactions: Prints all transaction data in a formatted table. Can view all or by year.
 - Update Transactions: Select a transaction to update and then update a specified field. All inputs are validated programmatically to preserve data integrity.
 - Delete Transactions: Delete a specified transaction from working list.
 - Analyze Transactions: Transactional data can be anayled as a whole or by specified year. Debits, Credits, and Transfers are individually summed and Net Balance is calculated.
 - Save Transactions: After manipulating transactional data, the working list can be saved to the original csv. Randomized test data can also be saved to this file. A backup file of original transactions is created to prevent accidental data loss. All old backup files are deleted.
 - Generate Report: A text file report is generated with a date stamp to promote clarity. Each new report will replace the old one. This feature can be turned off with a one-liner in case user wants to save old reports. Reports will include date range of transactions, a financial summary, percentage of transactions types against the total of transactions, a printout of the customers with the highest transactions per type (as well as the number associated), transaction totals by customer id, and finally the transactions sorted by date.
## Useage
 - Main Menu: Program starts with the above listed menu, where you select an option by entering a number 0-9.
 - 'ctrl+c' can be entered at any time to gracefully exit the program.
 - 'c' can be entered during any user prompt to exit back to Main Menu.  
0. Generate Test Transactions:
   - Generates a random set up data in valid structure.
   - Prompts for number of transactions to be generated.
   - This will clear any previously loaded transactions.    
1. Load Transactions:
   - Loads a set of transactional data from a csv file.
   - Checks for valid headers.
   - If headers are not valid it will also check to see if the top row contains valid data.
   - Will skip any rows that contain invalid or missing data and log details to console and error_log.txt    
2. Add Transaction:
   - Prompts inputs to add a new transaction.
   - Validation for all fields occurs.
   - New transaction is given an incremented unique transaction id.
   - Transaction is appended to working list.   
3. View Transactions:
   - Prompts to view transactions.
   - transactions can be viewed all at once or by a specific type ex: debit, credit, transfer.
   - Transactions will be printed to console in a formatted table.   
4. Update Transaction:
    - Displays transactions in a numbered list and prompts to select one to update.
    - Prompts for field to update and prompts for value.
    - Validation will occur on all inputs.   
5. Delete Transaction:
   - Displays transactions in a numbered list and prompts to select one to delete.
   - Prompts for certainty of deletion before actually deleting transaction from working list.   
6. Analyze Finances:
   - Prompts for transactions to analyze.
   - This can be done for all transactions or by year.
   - A financial summary of type totals and net balance will be printed.    
7. Save Transactions:
   - Saves working transaction list to original csv file location.
   - A backup of original file will be saved.
   - Old backup files are deleted before new one is saved.
   - Backups will be saved with current date/time stamp appended to file name.    
8. Generate Report:
   - A text file report is generated with a date stamp to promote clarity.
   - Each new report will replace the old one.
   - Report will include
     - Date range of transactions
     - Financial summary
     - Percentage of transactions types against the total of transactions
     - Printout of the customers with the highest transactions per type (as well as the number associated)
     - Transaction totals by customer id
     - Transactions sorted by date.
9. Exit: This will gracefully exit the program.   
## Development
 - Requirements: python 3.8+, Git.
 - Testing: Manually test with large datasets, invalid data structure, invalid inputs, and duplicate IDs.
 - Coding style: Follow PEP 8, user type hints, and provide robust validation and error handling.
## Contact
For issues or suggestions contact joshroehrig@gmail.com



