numbers = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]

# --- Step 1 & 2: Search on unsorted list ---
# Sequential (Linear) search is used because the list is unsorted.
# Linear search checks items sequentially without needing pre-sorted data.
def sequential_search(target, items):
    for index in range(len(items)):
        if items[index] == target:
            return index
    return None

target = 9
index_unsorted = sequential_search(target, numbers)
print(f"Linear Search: Number {target} found at index {index_unsorted} in the unsorted list.")


# --- Step 3: Insertion Sort Implementation ---
def insertion_sort(items):
    for i in range(1, len(items)):
        key = items[i]
        j = i - 1
        while j >= 0 and items[j] > key:
            items[j + 1] = items[j]
            j -= 1
        items[j + 1] = key
    return items

sorted_numbers = insertion_sort(numbers.copy())
print("Sorted list:", sorted_numbers)


# --- Step 4: Binary Search on sorted list ---
# Binary Search reduces search time to O(log n) by repeatedly dividing the search interval in half.
# Real-world usage: Used in database indexing, dictionary/phonebook lookups, and autocompletion systems where data is pre-sorted.
def binary_search(target, items):
    low, high = 0, len(items) - 1
    while low <= high:
        mid = (low + high) // 2
        if items[mid] == target:
            return mid
        elif items[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return None

index_sorted = binary_search(target, sorted_numbers)
print(f"Binary Search: Number {target} found at index {index_sorted} in the sorted list.")