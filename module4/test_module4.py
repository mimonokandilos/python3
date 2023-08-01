# test_module4.py

from file_handling import read_file, write_file
from exception_handling import division

def test_file_handling():
    # Test read_file() function with correct filename
    content = read_file("sample.txt")
    assert content == "Hello, this is a sample text file."

    # Test non-existent file
    content = read_file("non_existent_file.txt")
    assert content == "Error: File 'non_existent_file.txt' not found."

    # Test write_file() function
    result = write_file("output.txt", "This is the content of the output file.")
    assert result == "File write successful."

def test_exception_handling():
    # Test division() function
    result = division(10, 2)
    assert result == 5.0

    # Test division by zero
    result = division(10, 0)
    assert result == "Error: Cannot divide by zero."

if __name__ == "__main__":
    test_file_handling()
    test_exception_handling()
    print("All test cases passed successfully.")

