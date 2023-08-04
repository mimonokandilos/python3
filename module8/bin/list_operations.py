# list_operations.py

def find_max(numbers):
    if not numbers:
        raise ValueError("List is empty.")
    return max(numbers)

def find_min(numbers):
    if not numbers:
        raise ValueError("List is empty.")
    return min(numbers)

def average(numbers):
    if not numbers:
        raise ValueError("List is empty.")
    return sum(numbers) / len(numbers)

