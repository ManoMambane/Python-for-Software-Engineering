friends_names = ["John Smith", "Mary Jane", "Harry Potter"]

print(friends_names[0])
print(friends_names[-1])
print(len(friends_names))

friends_ages = [25, 28, 22]

for i in range(len(friends_names)):
    print(f"{friends_names[i]} is {friends_ages[i]} years old")