# Get favourite restaurant and number
string_fav = input("Enter your favourite restaurant: ")
int_fav = int(input("Enter your favourite number: "))

# Print both
print("Favourite Restaurant:", string_fav)
print("Favourite Number:", int_fav)

# Attempting to cast string_fav to an integer will fail:
# int(string_fav)
# Explanation: A ValueError occurs because text/alphabetical characters cannot be converted into an integer numeric data type.