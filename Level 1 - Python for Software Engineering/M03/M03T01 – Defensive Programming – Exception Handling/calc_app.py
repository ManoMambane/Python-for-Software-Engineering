def get_number(prompt_message):
    """Prompts the user for a valid floating-point number using exception handling."""
    while True:
        try:
            return float(input(prompt_message))
        except ValueError:
            print("Invalid input. Please enter a valid numerical value.")

def perform_calculation():
    """Handles number and operator input, computes the result, displays it, and writes to equations.txt."""
    num1 = get_number("Enter the first number: ")
    
    # Validate mathematical operator
    while True:
        operator = input("Enter an operator (+, -, *, /): ").strip()
        if operator in ['+', '-', '*', '/']:
            break
        print("Invalid operator. Please choose from +, -, *, or /.")

    # Defensive check for division by zero before prompting the second number
    while True:
        num2 = get_number("Enter the second number: ")
        if operator == '/' and num2 == 0:
            print("Error: Division by zero is not allowed. Please enter a non-zero denominator.")
        else:
            break

    # Calculate result
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2

    # Format numbers cleanly (strip unnecessary trailing decimal zeroes)
    fmt_num1 = int(num1) if num1.is_integer() else num1
    fmt_num2 = int(num2) if num2.is_integer() else num2
    fmt_result = int(result) if result.is_integer() else round(result, 4)

    equation_str = f"{fmt_num1} {operator} {fmt_num2} = {fmt_result}"
    print(f"\nResult: {equation_str}\n")

    # Append the calculated equation to equations.txt
    try:
        with open("equations.txt", "a") as file:
            file.write(equation_str + "\n")
    except IOError as e:
        print(f"Error writing to file: {e}")

def print_previous_equations():
    """Reads and displays all recorded calculations from equations.txt with defensive handling."""
    try:
        with open("equations.txt", "r") as file:
            content = file.read().strip()
            if content:
                print("\n--- Previous Calculations ---")
                print(content)
                print("-----------------------------\n")
            else:
                print("\nThe file 'equations.txt' is empty. No previous calculations found.\n")
    except FileNotFoundError:
        print("\nNo previous calculations found. 'equations.txt' does not exist yet.\n")

def main():
    """Main menu loop for the calculator application."""
    while True:
        print("=== Calculator Application ===")
        print("1. Perform a calculation")
        print("2. Print previous calculations")
        print("3. Exit")
        
        choice = input("Select an option (1-3): ").strip()

        if choice == '1':
            perform_calculation()
        elif choice == '2':
            print_previous_equations()
        elif choice == '3':
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid option. Please enter 1, 2, or 3.\n")

if __name__ == "__main__":
    main()