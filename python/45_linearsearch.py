
"""
Linear Search Algorithm in Python.
Searches for an element in a list using linear search.
"""

from typing import List

def linear_search(array: List[int], x: int) -> int:
    """
    Searches for x in array using linear search.
    Args:
        array (List[int]): List of integers to search.
        x (int): Element to find.
    Returns:
        int: Index of x if found, else -1.
    """
    for i, value in enumerate(array):
        if value == x:
            return i
    return -1


if __name__ == "__main__":
    array = [2, 4, 0, 1, 9]
    x = 1
    result = linear_search(array, x)
    if result == -1:
        print("Element not found")
    else:
        print("Element found at index:", result)
