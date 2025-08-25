from typing import List

"""
Bubble Sort Algorithm in Python.
Sorts a list in ascending order using bubble sort.
"""


def bubble_sort(array: List[int]) -> None:
    """
    Sorts the input list in ascending order using bubble sort.
    Args:
        array (List[int]): List of integers to sort.
    """
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


if __name__ == "__main__":
    data = [-2, 45, 0, 11, -9]
    bubble_sort(data)
    print('Sorted Array in Ascending Order:')
    print(data)
