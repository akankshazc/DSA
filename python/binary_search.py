from typing import List
"""
Binary Search Algorithm in Python.
Searches for an element in a sorted list using binary search.
"""


def binary_search(array: List[int], target: int) -> int:
    """
    Searches for x in array using binary search.
    Args:
        array (List[int]): Sorted list of integers to search.
        target (int): Element to find.
    Returns:
        int: Index of x if found, else -1.
    """
    low = 0
    high = len(array) - 1

    while high >= low:
        mid = (high + low) // 2
        if target == array[mid]:
            return mid
        elif target < array[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1


if __name__ == "__main__":
    array = [3, 4, 5, 5, 6, 7, 8, 9]
    x = 4
    result = binary_search(array, x)
    if result != -1:
        print(f"Element is present at index {result}")
    else:
        print("Not found")
