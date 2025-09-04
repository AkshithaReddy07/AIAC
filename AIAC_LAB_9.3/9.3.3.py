def add(a, b):
    """Return the sum of a and b."""
    return a + b

def subtract(a, b):
    """Return the difference of a and b."""
    return a - b

def multiply(a, b):
    """Return the product of a and b."""
    return a * b

def divide(a, b):
    """Return the quotient of a divided by b."""
    if b == 0:
        return "Error: Division by zero!"
    return a / b

def main():
    print("Simple Calculator")
    print("Available operations: add, subtract, multiply, divide")
    print("Type 'exit' to quit.\n")
    while True:
        operation = input("Enter operation (add/subtract/multiply/divide) or 'exit': ").strip().lower()
        if operation == 'exit':
            print("Exiting calculator. Goodbye!")
            break
        if operation not in ('add', 'subtract', 'multiply', 'divide'):
            print("Invalid operation. Please try again.")
            continue
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        if operation == 'add':
            result = add(a, b)
        elif operation == 'subtract':
            result = subtract(a, b)
        elif operation == 'multiply':
            result = multiply(a, b)
        elif operation == 'divide':
            result = divide(a, b)
        print(f"Result: {result}\n")

if __name__ == "__main__":
    main()
