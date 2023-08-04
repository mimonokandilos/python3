# file_handling.py

# Writing data to a file
def write_to_file(filename, data):
    with open(filename, 'w') as file:
        file.write(data)

# Reading data from a file
def read_from_file(filename):
    with open(filename, 'r') as file:
        return file.read()

# Test cases for file handling
if __name__ == "__main__":
    content = read_from_file("data.txt")
    print("Content read from file:", content)

