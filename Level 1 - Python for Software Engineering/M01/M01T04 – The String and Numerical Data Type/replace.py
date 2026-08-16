# Save the original string
sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."

# Replace exclamation marks with spaces
clean_sentence = sentence.replace("!", " ")
print(clean_sentence)

# Convert the string to uppercase
upper_sentence = clean_sentence.upper()
print(upper_sentence)

# Print the sentence in reverse using slicing
reversed_sentence = upper_sentence[::-1]
print(reversed_sentence)