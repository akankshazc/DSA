
"""
Merge Sort Algorithm in Python.
Sorts a list in ascending order using merge sort.
"""

from typing import List


def merge_sort(array: List[int]) -> None:
    """
    Sorts the input list in ascending order using merge sort.
    Args:
        array (List[int]): List of integers to sort.
    """
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1


def print_list(array: List[int]) -> None:
    """
    Prints the elements of the list separated by spaces.
    Args:
        array (List[int]): List of integers to print.
    """
    print(' '.join(str(x) for x in array))


if __name__ == "__main__":
    array = [6, 5, 12, 10, 9, 1]
    merge_sort(array)
    print("Sorted array is:")
    print_list(array)
