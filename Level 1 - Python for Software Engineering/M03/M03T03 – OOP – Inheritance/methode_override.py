# Parent Class
class Adult:
    def __init__(self, name, age, hair_color, eye_color):
        self.name = name
        self.age = age
        self.hair_color = hair_color
        self.eye_color = eye_color

    def can_drive(self):
        print(f"{self.name} is old enough to drive.")


# Subclass overriding the can_drive method
class Child(Adult):
    def can_drive(self):
        print(f"{self.name} is too young to drive.")


# Get user inputs
name = input("Enter name: ")
age = int(input("Enter age: "))
hair_color = input("Enter hair color: ")
eye_color = input("Enter eye color: ")

# Determine whether to instantiate Adult or Child based on age
if age >= 18:
    person = Adult(name, age, hair_color, eye_color)
else:
    person = Child(name, age, hair_color, eye_color)

# Call the can_drive method
person.can_drive()