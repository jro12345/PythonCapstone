def numbered_transaction_table(transactions: list[dict[str, any]]) -> None:
        """
        Displays a list of transactions as rows with transaction_id formatted as 'ID.' ex: '1.'
        Columns aligned based on maximum value length. 
        """
        columns = []
        # Calculates the max field length in transactions
        for key in transactions[0].keys():
            value_len = max(len(str(transaction.get(key, ''))) + 2 for transaction in transactions)
            columns.append((key, value_len))
        for transaction in transactions:
            line_parts = []
            cust=""
            for name, width in columns:
                # Format transaction_id with a period
                if name == "transaction_id":
                    cust = f"{str(transaction[name]) + '.':<{width}}"
                # Format and join rest of transaction row
                if name != "transaction_id":
                    value = f"{transaction[name]:.2f}" if name == "amount" else str(transaction[name])
                    line_parts.append(f" {value:<{width}}")
            # Join rest of transaction row with '|'
            line = '|'.join(line_parts)
            # Print entire transaction row
            print(cust+line)
        print()