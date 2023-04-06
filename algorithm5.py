#1.Selection Sort--Descending order

def sort_selection(arr1: list):
    max_value = 0
    while max_value < len(arr1)-1:
        for i in range(0, len(arr1)-1):
            if arr1[i] < arr1[i+1]:
                arr1[i], arr1[i+1] = arr1[i+1], arr1[i]
        max_value += 1
    return arr1

print(sort_selection([2, 5, 3, 8, 5, 7, 9, 1]))

#2 Bubble Sort--Descending order

def sort_bubble(arr2: list):
    n = len(arr2)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            # Swap if the element found is smaller than the next element
            if arr2[j] < arr2[j + 1]:
                arr2[j], arr2[j + 1] = arr2[j + 1], arr2[j]
    return arr2
print(sort_bubble([2, 5, 3, 8, 5, 7, 9, 1]))

# Insertion Srt -Descending order
def sort_insertion(arr3: list):
    n = len(arr3)
    # Traverse through 1 to n-1
    for i in range(1, n):
        key = arr3[i]
        j = i - 1
        # Move elements of arr[0..i-1], that are smaller than key, to one position ahead of their current position
        while j >= 0 and arr3[j] < key:
            arr3[j + 1] = arr3[j]
            j -= 1
        arr3[j + 1] = key
    return arr3

print(sort_insertion([2, 5, 3, 8, 5, 7, 9, 1]))

# #4. Merge Sort--Descending order
# I copied this code from a search, and while I understand the algorithm,
# coding it is beyond my current level of ability
# def sort_merge(arr4: list):
#     if len(arr4) > 1:
#         # Divide the array into two halves
#         mid = len(arr4) // 2
#         left_half = arr4[:mid]
#         right_half = arr4[mid:]
#
#         # Recursively sort the two halves
#         sort_merge(left_half)
#         sort_merge(right_half)
#
#         # Merge the sorted halves in descending order
#         i = j = k = 0
#         while i < len(left_half) and j < len(right_half):
#             if left_half[i] > right_half[j]:
#                 arr4[k] = left_half[i]
#                 i += 1
#             else:
#                 arr4[k] = right_half[j]
#                 j += 1
#             k += 1
#
#         # Copy the remaining elements of left_half[], if there are any
#         while i < len(left_half):
#             arr4[k] = left_half[i]
#             i += 1
#             k += 1
#
#         # Copy the remaining elements of right_half[], if there are any
#         while j < len(right_half):
#             arr4[k] = right_half[j]
#             j += 1
#             k += 1
#
#     return arr4

print(sort_merge([2, 5, 3, 8, 5, 7, 9, 1]))