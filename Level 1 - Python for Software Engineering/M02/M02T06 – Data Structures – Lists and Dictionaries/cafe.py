# 1. Define the menu items list
menu = ["Coffee", "Tea", "Sandwich", "Cake"]

# 2. Define stock quantity for each item
stock = {
    "Coffee": 100,
    "Tea": 50,
    "Sandwich": 20,
    "Cake": 15
}

# 3. Define price per unit for each item
price = {
    "Coffee": 2.50,
    "Tea": 2.00,
    "Sandwich": 5.00,
    "Cake": 3.50
}

# 4. Calculate total stock value across all items
total_stock = 0.0

for item in menu:
    item_value = stock[item] * price[item]
    total_stock += item_value

# 5. Output total stock worth
print(f"Total worth of stock in the café: ${total_stock:.2f}")