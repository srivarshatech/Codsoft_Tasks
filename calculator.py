def display_menu():
    """Displays the calculator menu."""
    print("=" * 35)
    print("      SIMPLE CALCULATOR")
    print("=" * 35)

    print("\nSelect an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

def get_numbers():
    """Takes two numbers from the user and returns them."""
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            return num1, num2
        except ValueError:
            print("Invalid number entered. Please try again.")
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            return num1, num2
        except ValueError:
            print("Invalid number entered. Please try again.")

def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    if num2 == 0:
        return None
    return num1 / num2

print("Welcome to the Python Calculator!")

def main():
    while True:
        display_menu()

        choice = input("Enter choice (1-5): ")

        if choice == "5":
            print("Thank you for using the calculator!")
            break

        if choice not in ("1", "2", "3", "4"):
            print("Invalid choice!")
            continue

        num1, num2 = get_numbers()
        if choice == "1":
            result = add(num1, num2)
        elif choice == "2":
            result = subtract(num1, num2)
        elif choice == "3":
            result = multiply(num1, num2)
        elif choice == "4":
            result = divide(num1, num2)

        if result is None:
            print("Error: Cannot divide by zero.")
        else:
            print("-" * 35)
            print(f"Result: {result:.2f}")
            print("-" * 35)

        # Ask user whether to continue; validate input
        while True:
            continue_choice = input("\nDo you want to continue? (y/n): ").lower()
            if continue_choice in ("y", "n"):
                break
            print("Please enter only 'y' or 'n'.")

        if continue_choice == "n":
            print("Thank you for using the calculator!")
            break

if __name__ == "__main__":
    main()