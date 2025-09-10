# Create a file with some records
with open("data.txt", "w") as file:
    file.writelines(["John\n", "Maria\n", "Peter\n", "Lucy\n"])

# Sequential search in the file
def sequential_search_file(filename, value):
    with open(filename, "r") as file:
        for i, line in enumerate(file):
            if line.strip() == value:  # Compare without extra spaces or newlines
                return i  # Return the line number where the value was found
    return -1  # Return -1 if the value is not found

# Perform the search
result = sequential_search_file("data.txt", "Lucy")
if result != -1:
    print(f"Element found at line {result + 1}")
else:
    print("Element not found")