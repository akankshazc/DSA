"""
Insertion Sort Algorithm in Python.
Sorts a list in ascending order using insertion sort.
"""

from typing import List


def insertion_sort(array: List[int]) -> None:
    """
    Sorts the input list in ascending order using insertion sort.
    Args:
        array (List[int]): List of integers to sort.
    """
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key


if __name__ == "__main__":
    data = [9, 5, 1, 4, 3]
    insertion_sort(data)
    print('Sorted Array in Ascending Order:')
    print(data)
