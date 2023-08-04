# exception_handling.py

# Divide two numbers and handle ZeroDivisionError
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = "Cannot divide by zero"
    finally:
        return result

# Test cases for exception handling
if __name__ == "__main__":
    print("TestCase 1: divide(10, 2)", divide(10, 2))
    print("TestCase 2: divide(5, 0)",divide(5, 0))

