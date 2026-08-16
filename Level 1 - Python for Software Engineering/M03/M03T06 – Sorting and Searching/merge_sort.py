def merge_sort(items):
    items_length = len(items)
    temporary_storage = [None] * items_length
    size_of_subsections = 1

    while size_of_subsections < items_length:
        for i in range(0, items_length, size_of_subsections * 2):
            first_section_start, first_section_end = i, min(
                i + size_of_subsections, items_length
            )
            second_section_start, second_section_end = first_section_end, min(
                first_section_end + size_of_subsections, items_length
            )
            sections = (first_section_start, first_section_end), (
                second_section_start,
                second_section_end,
            )
            merge(items, sections, temporary_storage)
        size_of_subsections *= 2
    return items


def merge(items, sections, temporary_storage):
    (first_section_start, first_section_end), (
        second_section_start,
        second_section_end,
    ) = sections

    left_index = first_section_start
    right_index = second_section_start
    temp_index = 0

    while left_index < first_section_end or right_index < second_section_end:
        if left_index < first_section_end and right_index < second_section_end:
            # Modified condition to sort by string length from longest to shortest
            if len(items[left_index]) >= len(items[right_index]):
                temporary_storage[temp_index] = items[left_index]
                left_index += 1
            else:
                temporary_storage[temp_index] = items[right_index]
                right_index += 1
            temp_index += 1
        elif left_index < first_section_end:
            for i in range(left_index, first_section_end):
                temporary_storage[temp_index] = items[left_index]
                left_index += 1
                temp_index += 1
        else:
            for i in range(right_index, second_section_end):
                temporary_storage[temp_index] = items[right_index]
                right_index += 1
                temp_index += 1

    for i in range(temp_index):
        items[first_section_start + i] = temporary_storage[i]


# 3 unsorted test lists with at least 10 elements each
list1 = ["apple", "dragonfruit", "fig", "banana", "watermelon", "kiwi", "elderberry", "date", "cherry", "grape"]
list2 = ["python", "c", "java", "javascript", "typescript", "ruby", "go", "kotlin", "swift", "rust"]
list3 = ["elephant", "cat", "hippopotamus", "dog", "rhinoceros", "ox", "giraffe", "ant", "kangaroo", "lion"]

print("List 1 Sorted:", merge_sort(list1))
print("List 2 Sorted:", merge_sort(list2))
print("List 3 Sorted:", merge_sort(list3))