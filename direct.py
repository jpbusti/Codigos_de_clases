import os
import json

# Function to write a record at a direct location
def write_record(file_name, record):
    """
    Writes a record to a file at a specific position based on its unique ID.
    """
    # Calculate the position using the hash of the record's ID
    record_id = record['id']
    position = hash(record_id) % 100  # Example: position within 100 slots
    print(position)

    with open(file_name, 'r+b') as file:
        # Seek to the calculated position
        file.seek(position * 100)  # Assume each record is 100 bytes max
        # Write the record as a fixed-size string
        record_str = json.dumps(record).ljust(100)
        print(record_str)
        file.write(record_str.encode('utf-8'))


# Function to read a record by ID
def read_record(file_name, record_id):
    """
    Reads a record from the file based on its unique ID.
    """
    position = hash(record_id) % 100

    with open(file_name, 'rb') as file:
        file.seek(position * 100)
        record_data = file.read(100).decode('utf-8').strip()

        if record_data:
            return json.loads(record_data)
        else:
            return None


# Function to create a blank file for direct access
def initialize_file(file_name, size=100):
    """
    Initializes a blank file with empty slots for direct access.
    """
    with open(file_name, 'wb') as file:
        file.write(b'\x00' * (size * 100))  # Reserve 100 bytes per slot


# Main function to demonstrate direct file organization
def main():
    file_name = "direct_access_file.dat"
    print(hash('Alice') % 100)

    initialize_file(file_name)

    # Add records to the file
    write_record(file_name, {'id': 'R001', 'name': 'Alice', 'balance': 500.75})
    write_record(file_name, {'id': 'R002', 'name': 'Bob', 'balance': 300.50})
    write_record(file_name, {'id': 'R003', 'name': 'Charlie', 'balance': 150.25})


    # Retrieve and display records
    print("Reading records directly:")
    print(read_record(file_name, 'R002'))
    print(read_record(file_name, 'R001'))
    print(read_record(file_name, 'R003'))
    #print(read_record(file_name, 'R999'))  # Non-existent record
    print(hash('R001') % 100)

if __name__ == "__main__":
    main()