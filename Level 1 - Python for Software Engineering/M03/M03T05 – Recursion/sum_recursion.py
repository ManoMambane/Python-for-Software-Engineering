def adding_up_to(numbers, index):
    # Base case: if index is 0, return the first element
    if index == 0:
        return numbers[0]
    # Recursive case: add current element to the sum of preceding elements
    return numbers[index] + adding_up_to(numbers, index - 1)


# Examples
if __name__ == "__main__":
    print(adding_up_to([1, 4, 5, 3, 12, 16], 4))  # Output: 25
    print(adding_up_to([4, 3, 1, 5], 1))          # Output: 7