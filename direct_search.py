# Create a file with records (key-value format)
with open("data.txt", "w") as file:
    file.writelines([
        "1,John\n",
        "2,Maria\n",
        "3,Peter\n",
        "4,Lucy\n"
    ])

# Load the file into a dictionary for direct search
def load_file_to_dict(filename):
    data_dict = {}
    with open(filename, "r") as file:
        for line in file:
            key, value = line.strip().split(",")  # Split the line into key and value
            data_dict[key] = value  # Store key-value pairs in the dictionary
    return data_dict

# Direct search function
def direct_search(data_dict, key):
    return data_dict.get(key, "Element not found") 

# Load data into a dictionary
data = load_file_to_dict("data.txt")

# Perform a direct search
key_to_search = "3"
result = direct_search(data, key_to_search)
print(f"Search result for key '{key_to_search}': {result}")