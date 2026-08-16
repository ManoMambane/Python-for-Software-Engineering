# Initialize an empty list to store incorrect names
incorrect_names = []

# Continuously prompt for a name until "John" is entered
while True:
    name = input("Enter your name: ")
    
    # Case-insensitive check for "John"
    if name.strip().lower() == "john":
        break
    
    # Store the incorrectly entered name
    incorrect_names.append(name)

# Display the list of incorrect names
print(f"Incorrect names: {incorrect_names}")