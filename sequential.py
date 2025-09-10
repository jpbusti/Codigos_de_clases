def truncate_file(file_name):
    """
    Truncates (empties) the file content, leaving it blank.
    """
    with open(file_name, 'w') as file:
        # The file is automatically emptied when opened in 'w' mode.
        pass

# Function to add transaction records to the sequential file
def add_transaction(file_name, transaction):
    """
    Adds a new transaction to the file sequentially.
    """
    with open(file_name, 'a') as file:  # 'a' is for append mode
        file.write(f"{transaction['id']},{transaction['date']},{transaction['amount']}\n")


# Function to read all transactions in sequential order
def read_transactions(file_name):
    """
    Reads all transactions stored in the file.
    """
    transactions = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                # Split each line by commas to extract the fields
                transaction_id, date, amount = line.strip().split(',')
                transactions.append({
                    'id': transaction_id,
                    'date': date,
                    'amount': float(amount)
                })
    except FileNotFoundError:
        print("The file does not exist. Please add a transaction first.")
    return transactions


# Main function to test sequential file organization
def main():
    transaction_file = "sequential_transactions.txt"
    truncate_file(transaction_file)
    # Add transactions to the file
    add_transaction(transaction_file, {'id': 'T001', 'date': '2025-01-01', 'amount': 100.50})
    add_transaction(transaction_file, {'id': 'T002', 'date': '2025-01-02', 'amount': 300.75})
    add_transaction(transaction_file, {'id': 'T003', 'date': '2025-01-03', 'amount': 150.25})

    # Read and display all transactions
    transactions = read_transactions(transaction_file)
    print("Transactions stored sequentially:")
    for transaction in transactions:
        print(transaction)


if __name__ == "__main__":
    main()