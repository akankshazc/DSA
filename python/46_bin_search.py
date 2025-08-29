from typing import List
"""
Binary Search Algorithm in Python.
Searches for an element in a sorted list using binary search (recursive).
"""


def binary_search(array: List[int], x: int, low: int, high: int) -> int:
    """
    Searches for x in array using recursive binary search.
    Args:
        array (List[int]): Sorted list of integers to search.
        x (int): Element to find.
        low (int): Starting index.
        high (int): Ending index.
    Returns:
        int: Index of x if found, else -1.
    """
    if high >= low:
        mid = low + (high - low) // 2
        if x == array[mid]:
            return mid
        elif x > array[mid]:
            return binary_search(array, x, mid + 1, high)
        else:
            return binary_search(array, x, low, mid - 1)
    else:
        return -1


if __name__ == "__main__":
    array = [3, 4, 5, 6, 7, 8, 9]
    x = 4
    result = binary_search(array, x, 0, len(array) - 1)
    if result != -1:
        print(f"Element is present at index {result}")
    else:
        print("Not found")
