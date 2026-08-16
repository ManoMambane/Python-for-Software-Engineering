String = "Hello"
print(String[0])
print(String[1])
print(String[2])
print(String[3])
print(String[4])

original_string = "Hello world!"
new_string = original_string[0:5]
print(new_string)
print(original_string)

print("Hello \n\"Bob\"")

print("The escape sequence \\n creates a new line in a print statement")

number_builder = ""
i = 0
while i <= 50:
    if i % 2 == 0:
        number_builder += str(i) + " "
    i += 1
print(number_builder)

number_builder = []
i = 0
while i <= 50:
    if i % 2 == 0:
        number_builder.append(str(i))
    i += 1
print(" ".join(number_builder))