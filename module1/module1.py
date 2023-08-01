# module1.py

# 1. Variables and Data Types

def data_types_demo():
    name = "John"  # String variable
    age = 25       # Integer variable
    height = 5.11  # Floating-point variable

    print("Name:", name)
    print("Age:", age)
    print("Height:", height)


# 2. Input and Output

def input_output_demo():
    print("Hello, World!")
    user_name = input("Enter your name: ")
    print("Hello,", user_name)


# 3. Conditional Statements (if-else)

def conditional_demo(age):
    if age >= 18:
        print("You are an adult.")
    else:
        print("You are a minor.")


# 4. Loops (for and while)

def loops_demo():
    # For loop to print numbers from 1 to 5
    print("Using for loop:")
    for i in range(1, 6):
        print(i)

    # While loop to print numbers from 1 to 5
    print("Using while loop:")
    count = 1
    while count <= 5:
        print(count)
        count += 1


# 5. Functions

def add_numbers(a, b):
    return a + b


# 6. Basic Debugging Techniques

def debugging_demo():
    # Uncomment the line below to demonstrate a runtime error (division by zero)
    # print(10 / 0)

    # Uncomment the lines below to demonstrate a logical error
    num1 = 5
    num2 = "2"
    print(num1 + num2)

    # Uncomment the lines below to demonstrate a syntax error
    # if True
    #     print("Syntax error")


# Test module1.py functions

if __name__ == "__main__":
    print("--- Data Types ---")
    data_types_demo()

    print("\n--- Input and Output ---")
    input_output_demo()

    print("\n--- Conditional Statements ---")
    age = int(input("Enter your age: "))
    conditional_demo(age)

    print("\n--- Loops ---")
    loops_demo()

    print("\n--- Functions ---")
    result = add_numbers(3, 7)
    print("Sum:", result)

    print("\n--- Debugging ---")
    debugging_demo()

