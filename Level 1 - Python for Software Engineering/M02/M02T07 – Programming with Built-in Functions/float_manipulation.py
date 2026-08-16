import statistics

# Collect 10 float inputs from the user and store them in a list
numbers = []
for i in range(10):
    num = float(input(f"Enter float {i + 1}: "))
    numbers.append(num)

# 1. Total of all numbers
total_sum = sum(numbers)
print(f"Total sum: {total_sum}")

# 2. Index of the maximum value
max_val = max(numbers)
max_index = numbers.index(max_val)
print(f"Index of maximum value ({max_val}): {max_index}")

# 3. Index of the minimum value
min_val = min(numbers)
min_index = numbers.index(min_val)
print(f"Index of minimum value ({min_val}): {min_index}")

# 4. Average (mean) rounded to two decimal places
mean_val = statistics.mean(numbers)
print(f"Average (mean): {round(mean_val, 2)}")

# 5. Median number
median_val = statistics.median(numbers)
print(f"Median: {median_val}")