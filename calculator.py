# Python Calculator - Portfolio Project
# Violah Kiconco

from colorama import init, Fore, Style
init(autoreset=True)

history = []

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Cannot divide by zero."
    return x / y

def power(x, y):
    return x ** y

def percentage(x, y):
    return (x * y) / 100

def show_history():
    if not history:
        print(Fore.YELLOW + "No calculations yet.")
    else:
        print(Fore.CYAN + "=== Calculation History ===")
        for record in history:
            print(record)
        print(Fore.CYAN + "==========================")

def calculator():
    print(Fore.GREEN + "="*40)
    print(Fore.GREEN + "      Violah's Premium Calculator")
    print(Fore.GREEN + "="*40)

    while True:
        print(Fore.MAGENTA + "\nSelect operation:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Power (^)")
        print("6. Percentage (%)")
        print("7. Show History")
        print("8. Exit")

        choice = input(Fore.BLUE + "Enter choice (1-8): ")

        if choice == '8':
            print(Fore.GREEN + "Thank you for using the calculator! Goodbye.")
            break

        if choice not in [str(i) for i in range(1, 8)]:
            print(Fore.RED + "Invalid choice! Try again.")
            continue

        if choice == '7':
            show_history()
            continue

        try:
            num1 = float(input(Fore.YELLOW + "Enter first number: "))
            num2 = float(input(Fore.YELLOW + "Enter second number: "))
        except ValueError:
            print(Fore.RED + "Error! Please enter a valid number.")
            continue

        if choice == '1':
            result = add(num1, num2)
            operation = f"{num1} + {num2} = {result}"
        elif choice == '2':
            result = subtract(num1, num2)
            operation = f"{num1} - {num2} = {result}"
        elif choice == '3':
            result = multiply(num1, num2)
            operation = f"{num1} * {num2} = {result}"
        elif choice == '4':
            result = divide(num1, num2)
            operation = f"{num1} / {num2} = {result}"
        elif choice == '5':
            result = power(num1, num2)
            operation = f"{num1} ^ {num2} = {result}"
        elif choice == '6':
            result = percentage(num1, num2)
            operation = f"{num2}% of {num1} = {result}"

        print(Fore.GREEN + f"Result: {result}")
        history.append(operation)

        # Save to file
        with open("calculator_history.txt", "w") as f:
            for record in history:
                f.write(record + "\n")

calculator()