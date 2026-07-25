"""
Week 1 - Simple Command Line Calculator
Supports: add, subtract, multiply, divide
"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b


def main():
    print("=== Simple CLI Calculator ===")
    print("Operations: + , - , * , /")
    print("Type 'exit' to quit\n")

    while True:
        user_input = input("Enter calculation (e.g. 5 + 3): ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        try:
            parts = user_input.split()
            if len(parts) != 3:
                print("Invalid format. Use: number operator number")
                continue

            num1, operator, num2 = parts
            num1 = float(num1)
            num2 = float(num2)

            if operator == "+":
                result = add(num1, num2)
            elif operator == "-":
                result = subtract(num1, num2)
            elif operator == "*":
                result = multiply(num1, num2)
            elif operator == "/":
                result = divide(num1, num2)
            else:
                print("Invalid operator. Use one of + - * /")
                continue

            print(f"Result: {result}\n")

        except ValueError:
            print("Invalid numbers entered. Try again.\n")


if __name__ == "__main__":
    main()