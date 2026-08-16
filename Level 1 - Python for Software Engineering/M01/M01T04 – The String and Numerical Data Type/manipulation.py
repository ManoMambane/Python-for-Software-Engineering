# Prompt user for input
str_manip = input("Enter a sentence: ")

# 1. Calculate and display the length of the string
print("Length of sentence:", len(str_manip))

# 2. Replace every occurrence of the last letter with '@'
last_letter = str_manip[-1]
modified_str = str_manip.replace(last_letter, "@")
print(modified_str)

# 3. Print the last 3 characters backwards
last_three_reversed = str_manip[-1:-4:-1]
print(last_three_reversed)

# 4. Create a 5-letter word from the first 3 and last 2 characters
five_letter_word = str_manip[:3] + str_manip[-2:]
print(five_letter_word)