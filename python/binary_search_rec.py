from typing import List
"""
Binary Search Algorithm in Python.
Searches for an element in a sorted list using binary search (recursive).
"""


def binary_search_rec(array: List[int], target: int, low: int, high: int) -> int:
    """
    Searches for x in array using binary search.
    Args:
        array (List[int]): Sorted list of integers to search.
        target (int): Element to find.
        low (int): lower index of the array.
        high (int): highest index of the array.
    Returns:
        int: Index of x if found, else -1.
    """
    if high >= low:
        mid = (high + low) // 2
        guess = array[mid]

        # check base case
        if guess == target:
            return mid
        elif guess > target:
            return binary_search_rec(array, target, low, mid - 1)
        else:
            return binary_search_rec(array, target, mid + 1, high)
    else:
        return -1


if __name__ == "__main__":
    array = [3, 4, 5, 5, 6, 7, 8, 9]
    x = 6
    result = binary_search_rec(array, x, 0, len(array)-1)
    if result != -1:
        print(f"Element is present at index {result}")
    else:
        print("Not found")
