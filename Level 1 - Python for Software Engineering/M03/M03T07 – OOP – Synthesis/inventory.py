"""
Nike Warehouse Inventory Management System
File: inventory.py
Description: OOP implementation for reading, searching, updating, and 
analyzing shoe stock data from inventory.txt.
"""

import sys

# Optional import for formatted tabulate output if installed
try:
    from tabulate import tabulate
    HAS_TABULATE = True
except ImportError:
    HAS_TABULATE = False


# ========The beginning of the class==========
class Shoe:
    """Represents a shoe item stored in the warehouse inventory."""

    def __init__(self, country, code, product, cost, quantity):
        """Initializes shoe details including cost (float) and quantity (int)."""
        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost)
        self.quantity = int(quantity)

    def get_cost(self):
        """Returns the cost of the shoe."""
        return self.cost

    def get_quantity(self):
        """Returns the available quantity of the shoe."""
        return self.quantity

    def __str__(self):
        """Returns a string representation of the Shoe object."""
        return (
            f"Country: {self.country} | Code: {self.code} | "
            f"Product: {self.product} | Cost: R{self.cost:.2f} | "
            f"Quantity: {self.quantity}"
        )


# =============Shoe list===========
shoe_list = []


# ==========Functions outside the class==============
def read_shoes_data(filename="inventory.txt"):
    """
    Opens inventory.txt, parses shoe records, and appends Shoe objects to shoe_list.
    Skips the header line and handles file-related or format errors defensively.
    """
    shoe_list.clear()  # Clear existing list to prevent duplicates on reload
    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()
            if not lines:
                print("[ERROR] The inventory file is empty.")
                return

            # Skip header line
            for line_num, line in enumerate(lines[1:], start=2):
                line = line.strip()
                if not line:
                    continue  # Skip empty lines

                parts = line.split(",")
                if len(parts) == 5:
                    country, code, product, cost_str, qty_str = parts
                    try:
                        shoe_obj = Shoe(country, code, product, cost_str, qty_str)
                        shoe_list.append(shoe_obj)
                    except ValueError:
                        print(
                            f"[WARNING] Skipping row {line_num} due to invalid numeric data: '{line}'"
                        )
                else:
                    print(
                        f"[WARNING] Skipping row {line_num} due to incorrect column count: '{line}'"
                    )

        print(f"[SUCCESS] Successfully loaded {len(shoe_list)} items into inventory.")

    except FileNotFoundError:
        print(f"[ERROR] The file '{filename}' was not found. Please check the path.")
    except Exception as e:
        print(f"[ERROR] An unexpected error occurred while reading the file: {e}")


def capture_shoes():
    """
    Prompts the user to enter shoe details, creates a Shoe object,
    appends it to shoe_list, and appends it to inventory.txt.
    """
    print("\n--- Capture New Shoe Item ---")
    country = input("Enter Country: ").strip()
    code = input("Enter Shoe Code (e.g., SKU12345): ").strip().upper()
    product = input("Enter Product Name: ").strip()

    # Validate cost
    while True:
        try:
            cost = float(input("Enter Cost per unit: ").strip())
            if cost < 0:
                print("Cost cannot be negative. Try again.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid number for cost.")

    # Validate quantity
    while True:
        try:
            quantity = int(input("Enter Quantity: ").strip())
            if quantity < 0:
                print("Quantity cannot be negative. Try again.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid integer for quantity.")

    # Create object & append to list
    new_shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(new_shoe)

    # Persist to text file
    try:
        with open("inventory.txt", "a", encoding="utf-8") as file:
            file.write(f"\n{country},{code},{product},{cost},{quantity}")
        print(f"[SUCCESS] '{product}' added to inventory and saved to file.")
    except IOError as e:
        print(f"[ERROR] Could not save entry to file: {e}")


def view_all():
    """
    Prints details of all shoes in the inventory list.
    Displays as a formatted table if 'tabulate' is available, otherwise plain text.
    """
    if not shoe_list:
        print("\n[INFO] No inventory data available. Load or capture data first.")
        return

    print("\n======================= CURRENT INVENTORY =======================")

    if HAS_TABULATE:
        table_data = [
            [s.country, s.code, s.product, f"R{s.cost:.2f}", s.quantity]
            for s in shoe_list
        ]
        headers = ["Country", "Code", "Product", "Cost", "Quantity"]
        print(tabulate(table_data, headers=headers, tablefmt="grid"))
    else:
        for idx, shoe in enumerate(shoe_list, start=1):
            print(f"{idx:02d}. {shoe}")


def re_stock():
    """
    Finds the shoe object with the lowest quantity, asks the user if they 
    want to add stock, and updates both the object and inventory.txt.
    """
    if not shoe_list:
        print("\n[INFO] No inventory data loaded.")
        return

    # Find shoe with lowest quantity
    min_shoe = min(shoe_list, key=lambda shoe: shoe.get_quantity())

    print("\n--- Restock Recommendation ---")
    print(f"Lowest Stock Item: {min_shoe.product} ({min_shoe.code})")
    print(f"Current Quantity: {min_shoe.get_quantity()}")

    choice = input("\nWould you like to add stock for this item? (y/n): ").strip().lower()
    if choice in ['y', 'yes']:
        while True:
            try:
                add_qty = int(input("Enter additional quantity to add: ").strip())
                if add_qty <= 0:
                    print("Quantity added must be greater than zero.")
                    continue
                break
            except ValueError:
                print("Invalid input! Please enter a valid whole number.")

        # Update in-memory object
        min_shoe.quantity += add_qty

        # Write updated list back to inventory.txt
        _update_inventory_file()
        print(f"[SUCCESS] {min_shoe.product} restocked. New Quantity: {min_shoe.quantity}")
    else:
        print("Restock operation cancelled.")


def search_shoe():
    """
    Searches for a shoe by its product code and displays the result.
    """
    if not shoe_list:
        print("\n[INFO] No inventory data loaded.")
        return

    search_code = input("\nEnter Shoe Code to search (e.g., SKU44386): ").strip().upper()
    found_shoe = None

    for shoe in shoe_list:
        if shoe.code.upper() == search_code:
            found_shoe = shoe
            break

    if found_shoe:
        print("\n--- Product Found ---")
        print(found_shoe)
    else:
        print(f"\n[INFO] No product found matching code '{search_code}'.")


def value_per_item():
    """
    Calculates and displays total stock value (cost * quantity) for each item.
    """
    if not shoe_list:
        print("\n[INFO] No inventory data loaded.")
        return

    print("\n======================= TOTAL STOCK VALUE PER ITEM =======================")

    if HAS_TABULATE:
        table_data = [
            [s.code, s.product, f"R{s.cost:.2f}", s.quantity, f"R{(s.cost * s.quantity):,.2f}"]
            for s in shoe_list
        ]
        headers = ["Code", "Product", "Unit Cost", "Quantity", "Total Value"]
        print(tabulate(table_data, headers=headers, tablefmt="grid"))
    else:
        for shoe in shoe_list:
            total_val = shoe.get_cost() * shoe.get_quantity()
            print(f"Code: {shoe.code:<10} | Product: {shoe.product:<20} | Total Value: R{total_val:,.2f}")


def highest_qty():
    """
    Determines the shoe with the highest quantity and outputs it as being on sale.
    """
    if not shoe_list:
        print("\n[INFO] No inventory data loaded.")
        return

    max_shoe = max(shoe_list, key=lambda shoe: shoe.get_quantity())

    print("\n======================= FOR SALE / CLEARANCE =======================")
    print(f"🔥 SPECIAL SALE: {max_shoe.product} ({max_shoe.code})")
    print(f"Overstocked Quantity: {max_shoe.get_quantity()} units available!")
    print(f"Unit Price: R{max_shoe.get_cost():.2f}")


def _update_inventory_file(filename="inventory.txt"):
    """Helper method to overwrite inventory.txt with updated list data."""
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write("Country,Code,Product,Cost,Quantity\n")
            for shoe in shoe_list:
                file.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost:.0f},{shoe.quantity}\n")
    except IOError as e:
        print(f"[ERROR] Failed to update inventory file: {e}")


# ==========Main Menu=============
def main():
    """Main program execution loop."""
    # Automatically load stock data at startup
    read_shoes_data()

    while True:
        print("\n" + "=" * 45)
        print("     NIKE WAREHOUSE INVENTORY SYSTEM     ")
        print("=" * 45)
        print("1. View All Products")
        print("2. Capture New Shoe Item")
        print("3. Restock Lowest Quantity Item")
        print("4. Search Product by Code")
        print("5. Calculate Value per Item")
        print("6. Show Overstocked Item for Sale")
        print("7. Reload Inventory File")
        print("8. Exit System")
        print("=" * 45)

        user_choice = input("Select an option (1-8): ").strip()

        if user_choice == "1":
            view_all()
        elif user_choice == "2":
            capture_shoes()
        elif user_choice == "3":
            re_stock()
        elif user_choice == "4":
            search_shoe()
        elif user_choice == "5":
            value_per_item()
        elif user_choice == "6":
            highest_qty()
        elif user_choice == "7":
            read_shoes_data()
        elif user_choice == "8":
            print("\nThank you for using Nike Inventory System. Goodbye!")
            sys.exit()
        else:
            print("\n[ERROR] Invalid choice. Please enter a number between 1 and 8.")


if __name__ == "__main__":
    main()