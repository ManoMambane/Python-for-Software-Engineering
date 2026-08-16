import random

# List of setup and punchline joke tuples
jokes = [
    ("Why do Java developers wear glasses?", "Because they don't C#!"),
    ("Why do programmers prefer dark mode?", "Because light attracts bugs!"),
    ("How many programmers does it take to change a lightbulb?", "None. It's a hardware problem!"),
    ("There are 10 types of people in the world...", "Those who understand binary, and those who don't."),
    ("Why did the programmer quit his job?", "Because he didn't get arrays!")
]

# Select and display a random joke
setup, punchline = random.choice(jokes)
print(f"Joke: {setup}")
print(f"Punchline: {punchline}")