# main.py

# Import functions from data_structures.py
from data_structures import numbers_list, fruits_list, coordinates, unique_numbers_set, person_info

# Import functions from search_sort.py
from search_sort import linear_search, binary_search, bubble_sort

# Import functions from recursion.py
from recursion import factorial

# Test data structures
print("Numbers List:", numbers_list)
print("Fruits List:", fruits_list)
print("Coordinates Tuple:", coordinates)
print("Unique Numbers Set:", unique_numbers_set)
print("Person Info Dictionary:", person_info)

# Test searching and sorting algorithms
numbers = [4, 7, 1, 9, 3, 6]
target_number = 9

index = linear_search(numbers, target_number)
print(f"Linear Search: {target_number} found at index {index}")

bubble_sort(numbers)
print("Sorted List:", numbers)

# Test recursion
n = 5
print(f"Factorial of {n} is: {factorial(n)}")

