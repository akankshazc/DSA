"""
Optimized Bubble Sort Algorithm in Python.
Sorts a list in ascending order using bubble sort with early termination.
"""
from typing import List


def bubble_sort(array: List[int]) -> None:
    """
    Sorts the input list in ascending order using optimized bubble sort.
    Terminates early if the list is already sorted.
    Args:
        array (List[int]): List of integers to sort.
    """
    n = len(array)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if not swapped:
            break


if __name__ == "__main__":
    data = [-2, 45, 0, 11, -9]
    bubble_sort(data)
    print('Sorted Array in Ascending Order:')
    print(data)
