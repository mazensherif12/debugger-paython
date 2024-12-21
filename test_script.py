# test_script.py

def greet(name):
    message = f"Hello, {name}!"
    print(message)  # Correct usage

def add(a, b):
    try:
        result = int(a) + int(b)  # Fix: Convert inputs to integers
        print(f"The result is {result}")
    except ValueError:
        print("Error: Both inputs must be numbers.")

def divide(a, b):
    try:
        result = a / b  # Fix: Handle division by zero
        print(f"The result is {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

if __name__ == "__main__":
    greet("Alice")
    add(3, "5")  # Fix applied: Correct type conversion
    divide(10, 0)  # Fix applied: Zero division handled

    # Fix: Removed undefined function call
    print("All operations completed.")











