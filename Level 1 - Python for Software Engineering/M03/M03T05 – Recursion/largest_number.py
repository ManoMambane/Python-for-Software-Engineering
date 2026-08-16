def largest_number(numbers):
    # Base case: if the list has only one element, that element is the largest
    if len(numbers) == 1:
        return numbers[0]
    
    # Recursive step: find the largest number in the rest of the list
    max_of_rest = largest_number(numbers[1:])
    
    # Compare the first element with the max of the rest
    if numbers[0] > max_of_rest:
        return numbers[0]
    else:
        return max_of_rest


# Examples
if __name__ == "__main__":
    print(largest_number([1, 4, 5, 3]))            # Output: 5
    print(largest_number([3, 1, 6, 8, 2, 4, 5]))   # Output: 8