from datetime import datetime

def validate_transaction_id(value: any, previous_ids: list[any] = None) -> int:
    """ Validate value is a valid int > 0. """
    clean_value = value.strip()
    if previous_ids is None:
        previous_ids = []
    if not clean_value.isdigit():
        raise ValueError (f"\nInvalid transaction id {value}: transaction Id must be a positive integer.\n") 
    transaction_id = int(clean_value) 
    if transaction_id == 0:
        raise ValueError("\nTransaction id cannot be 0, it must be a postive integer.\n")
    if transaction_id in previous_ids:
        raise ValueError (f"\nYou can not have duplicate transaction ids. {transaction_id} is in list {previous_ids} already\n")
    return transaction_id

def validate_customer_id(value: any) -> int:
    """ Validate value is a postive int. """
    customer_id = value.strip() 
    if not customer_id.isdigit():
        raise ValueError (f"\nInvalid customer id {value}: customer Id must be a positive integer.\n")
    return int(customer_id)

def validate_date(value: any) -> datetime.date:
    """ Validate value is a datetime.date in YYYY-MM-DD format. """
    date = value.strip()
    try:
        return datetime.strptime(date, '%Y-%m-%d').date()
    except ValueError:
        raise ValueError(f"\nInvalid date {value}: Date must be valid and in correct format (YYYY-MM-DD).\n")

def validate_amount(value: any) -> float:
    """ Validate value is a positive float. """
    clean_value = value.strip()
    try:
        amount = float(clean_value)
        if amount <= 0:
            raise ValueError
        return round(amount, 2)
    except (ValueError):
        raise ValueError(f"\nInvalid transaction amount {value}: Transaction amount must be a positive number.\n")
    
def validate_transaction_type(value: any) -> str:
    """ Validate value is string in ('debit', 'credit', 'transfer'). """
    valid_transaction_types = ["debit", "credit", "transfer"]
    type = value.strip().lower()
    if type not in valid_transaction_types:
        raise ValueError(f"\nInvalid transaction type: '{value}'. Valid types are {valid_transaction_types}.\n")
    return type

def get_valid_input(prompt: any, validate_func: callable) -> callable:
    """ Generate user input promt and validate the input. """
    while True:
        try:
            # Prompt generated based on calling function parameter
            user_input = input(prompt).strip()
            if not user_input:
                raise ValueError("\nInput cannot be empty\n")
            # Return validation function based on calling function parameter
            return validate_func(user_input)
        except ValueError as e:
            print(e)

def get_valid_date() -> datetime.date:
    """ Prompt user for date and validate input. """
    prompt = "Enter date in format (YYYY-MM-DD): "
    # Call input validation func and pass in prompt and date validation func
    return get_valid_input(prompt, validate_date)

def get_valid_type() -> str:
    """ Prompt user for transaction type and validate input. """
    prompt = "Enter type (credit/debit/transfer): "
    # Call input validation func and pass in prompt and type validation func
    return get_valid_input(prompt, validate_transaction_type)

def get_valid_amount() -> float:
    """ Prompt user for amount and validate input. """
    prompt = "Enter amount: "
    # Call input validation func and pass in prompt and amount validation func
    return get_valid_input(prompt, validate_amount)

def get_valid_customer_id() -> int:
    """ Prompt user for customer id and validate input. """
    prompt = "Enter customer ID: "
    # Call input validation func and pass in prompt and customer id validation func
    return get_valid_input(prompt, validate_customer_id)
            
def validate_transactions_loaded(transactions: list[dict[str, any]]) -> bool:
    """ Validate transactions are not empty. """
    if not transactions:
        print("Transactions list is empty.")
        return False
    return True